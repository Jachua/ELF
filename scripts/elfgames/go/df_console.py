#!/usr/bin/env python

# Copyright (c) 2018-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.

import os
import sys

import torch

from console_lib import GoConsoleGTP
from rlpytorch import Evaluator, load_env

import grpc

import play_pb2
import play_pb2_grpc

from server_addrs import addrs   


def move2xy(v):
    if v.lower() == "pass":
        return -1, -1
    x = ord(v[0].lower()) - ord('a')
    # Skip 'i' 
    if x >= 9:
        x -= 1
    y = int(v[1:]) - 1
    return x, y

def xy2move(x, y):
    if x == -1 and y == -1:
        return "pass"

    if x >= 8:
        x += 1
    return chr(x + 65) + str(y + 1)


def main():
    address = addrs['game_server']
    if address != "":
        channel = grpc.insecure_channel(address + ':50051')
    else :
        channel = grpc.insecure_channel("localhost:50051")
    stub = play_pb2_grpc.TurnStub(channel)
    print('Python version:', sys.version)
    print('PyTorch version:', torch.__version__)
    print('CUDA version', torch.version.cuda)
    print('Conda env:', os.environ.get("CONDA_DEFAULT_ENV", ""))

    additional_to_load = {
        'evaluator': (
            Evaluator.get_option_spec(),
            lambda object_map: Evaluator(object_map, stats=None)),
    }

    # Set game to online model.
    env = load_env(
        os.environ,
        overrides={
            'num_games': 1,
            'greedy': True,
            'T': 1,
            'model': 'online',
            'additional_labels': ['aug_code', 'move_idx'],
        },
        additional_to_load=additional_to_load)

    evaluator = env['evaluator']

    GC = env["game"].initialize()

    model_loader = env["model_loaders"][0]
    model = model_loader.load_model(GC.params)

    mi = env['mi']
    mi.add_model("model", model)
    mi.add_model("actor", model)
    mi["model"].eval()
    mi["actor"].eval()

    console = GoConsoleGTP(GC, evaluator)

    # TODO: create an instance of game when the client sends a request

    # print("\n\n\nCheck connect\n\n\n")
    # ID = stub.NewRoom(play_pb2.State(status = True)).ID 
    # print("Current AI's ID is ", ID)


    # res_arr = stub.GetResumed(play_pb2.State(status = True, ID = ID)).move
    # console.res_len = len(res_arr)
    # # console.res_ind = 3
    # # arr = ["BKD", "WFB", "BGA"]
    # if console.res_len > 0 and res_arr[-1][0].upper() == "B":
    #     _ = stub.UpdateNext(play_pb2.State(status = True, ID = ID))    

    # def check_end_game(m):
    #     if m.quit:
    #         GC.stop()
    #     return m
    
    def reset():
        ID = stub.NewRoom(play_pb2.State(status = True)).ID 
        console.ID = ID
        console.color = {'has_chosen': False, "client": 1, "AI": 2}
        console.prev_player = 0
        print("Current AI's ID is ", console.ID)
        if not console.color["has_chosen"]:
            while not stub.HasChosen(play_pb2.State(status = True, ID = ID)).status:
                pass
            # AI_color = stub.GetAIPlayer(play_pb2.State(status = True)).color
            # human_color = AI_color % 2 + 1
            console.color["AI"] = stub.GetAIPlayer(play_pb2.State(status = True, ID = ID)).color
            console.color["client"] = console.color["AI"] % 2 + 1
            console.color["has_chosen"] = True
        console.res_arr = stub.GetResumed(play_pb2.State(status = True, ID = ID)).move
        console.res_len = len(console.res_arr)
        if console.res_len > 0 and console.res_arr[-1][0].upper() == "B":
            _ = stub.UpdateNext(play_pb2.State(status = True, ID = ID))    

    reset()

    def check_reset(reply):
        console.reset = stub.CheckExit(play_pb2.State(status = True, ID = console.ID)).status
        if console.reset:
            print("\n\n\nRestarting game...\n\n\n")
            reset()
            console.reset = False
            reply["a"] = console.actions["clear"]
            return True, reply
        return False, reply

    def human_actor(batch):
        # print("\n\n\nCheck human_actor\n\n\n")
        reply = dict(pi = None, a = None, V = 0)
        ID = console.ID
        # console.reset = stub.CheckExit(play_pb2.State(status = True, ID = ID)).status
        # if console.reset:
        #     print("\n\n\nRestarting game...\n\n\n")
        #     reset()
        #     console.reset = False
        #     reply["a"] = console.actions["clear"]
        #     return reply
        AI_color = console.color["AI"]
        human_color = console.color["client"]
        # is_resumed = stub.IsResumed(play_pb2.State(status = True)).status 
        if console.res_len > 0:
            # print("\n\n\nCheck is_resumed = true\n\n\n")
            # print("\n\n\n", arr[-console.res_ind], "\n\n\n")
            reply["a"] = console.str2action(console.res_arr[-console.res_len])
            console.res_len -= 1
            return reply
        # print("\n\n\nCheck is_resumed = false\n\n\n")    
        while True:
            if console.prev_player == 1:
                move = console.get_last_move(batch)
                x, y = move2xy(move)
                _ = stub.SetMove(play_pb2.Step(x = x, y = y, 
                player = play_pb2.Player(color =  AI_color, ID = ID)))
                _ = stub.UpdateNext(play_pb2.State(status = True, ID = ID))
            if stub.IsNextPlayer(play_pb2.Player(color = AI_color, ID = ID)).status:
                reply["a"] = console.actions["skip"]
                console.prev_player = 1
                return reply
            # else:
            while stub.IsNextPlayer(play_pb2.Player(color = human_color, ID = ID)).status:
                do_reset, reply = check_reset(reply)
                if do_reset:
                    return reply
                pass
            human_xy = stub.GetMove(play_pb2.Player(color = human_color, ID = ID))
            reply["a"] = console.move2action(xy2move(human_xy.x, human_xy.y))
            console.prev_player = 2
            return reply 

    def actor(batch):
        return console.actor(batch)

    def train(batch):
        console.prompt("DF Train> ", batch)

    evaluator.setup(sampler=env["sampler"], mi=mi)

    GC.reg_callback_if_exists("actor_black", actor)
    GC.reg_callback_if_exists("human_actor", human_actor)
    GC.reg_callback_if_exists("train", train)

    GC.start()
    GC.GC.getClient().setRequest(
        mi["actor"].step, -1, env['game'].options.resign_thres, -1)

    evaluator.episode_start(0)

    while True:
        GC.run()
        if console.exit:
            break
    GC.stop()


if __name__ == '__main__':
    main()