#!/usr/bin/env python

# Copyright (c) 2018-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.

# Console for DarkForest

import os
from rlpytorch import Evaluator, load_env
from console_lib import GoConsoleGTP

import grpc

import play_pb2
import play_pb2_grpc

from server_addrs import addrs   



if __name__ == '__main__':
    additional_to_load = {
        'evaluator': (
            Evaluator.get_option_spec(),
            lambda object_map: Evaluator(object_map, stats=None)),
    }

    # Set game to online model.
    env = load_env(
        os.environ,
        overrides=dict(
            num_games=1,
            greedy=True,
            T=1,
            model="online",
            additional_labels=['aug_code', 'move_idx'],
        ),
        additional_to_load=additional_to_load)

    evaluator = env['evaluator']

    GC = env["game"].initialize()

    model_loader = env["model_loaders"][0]
    model = model_loader.load_model(GC.params)

    gpu = model_loader.options.gpu
    use_gpu = gpu is not None and gpu >= 0

    mi = env['mi']
    mi.add_model("model", model)
    # mi.add_model(
    #     "actor", model,
    #     copy=True, cuda=use_gpu, gpu_id=gpu)
    mi.add_model("actor", model)
    mi["model"].eval()
    mi["actor"].eval()

    console = GoConsoleGTP(GC, evaluator)
    address = addrs['game_server']
    if address != "":
        channel = grpc.insecure_channel(address + ':50051')
    else :
        channel = grpc.insecure_channel("localhost:50051")
    stub = play_pb2_grpc.TurnStub(channel)
    # print("\n\n\nCheck connect\n\n\n")
    ID = stub.NewRoom(play_pb2.State(status = True)).ID 
    print("Current AI's ID is ", ID)

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

    res_arr = stub.GetResumed(play_pb2.State(status = True, ID = ID)).move
    console.res_len = len(res_arr)
    # console.res_ind = 3
    # arr = ["BKD", "WFB", "BGA"]
    if console.res_len > 0 and res_arr[-1][0].upper() == "B":
        _ = stub.UpdateNext(play_pb2.State(status = True, ID = ID))

    def human_actor(batch):
        # print("\n\n\nCheck human_actor\n\n\n")
        if not console.color["has_chosen"]:
            while not stub.HasChosen(play_pb2.State(status = True, ID = ID)).status:
                pass
            # AI_color = stub.GetAIPlayer(play_pb2.State(status = True)).color
            # human_color = AI_color % 2 + 1
            console.color["AI"] = stub.GetAIPlayer(play_pb2.State(status = True, ID = ID)).color
            console.color["client"] = console.color["AI"] % 2 + 1
            console.color["has_chosen"] = True
        AI_color = console.color["AI"]
        human_color = console.color["client"]
        reply = dict(pi = None, a = None, V = 0)
        # is_resumed = stub.IsResumed(play_pb2.State(status = True)).status 
        if console.res_len > 0:
            # print("\n\n\nCheck is_resumed = true\n\n\n")
            # print("\n\n\n", arr[-console.res_ind], "\n\n\n")
            reply["a"] = console.str2action(res_arr[-console.res_len])
            console.res_len -= 1
            return reply
        # print("\n\n\nCheck is_resumed = false\n\n\n")    
        while True:
            if console.prev_player == 1:
                move = console.get_last_move(batch)
                x, y = move2xy(move)
                _ = stub.SetMove(play_pb2.Step(x = x, y = y, player = play_pb2.Player(color =  AI_color, ID = ID)))
                _ = stub.UpdateNext(play_pb2.State(status = True, ID = ID))
            if stub.IsNextPlayer(play_pb2.Player(color = AI_color, ID = ID)).status:
                reply["a"] = console.actions["skip"]
                console.prev_player = 1
                return reply
            else:
                while stub.IsNextPlayer(play_pb2.Player(color = human_color, ID = ID)).status:
                    pass
                human_xy = stub.GetMove(play_pb2.Player(color = human_color, ID = ID))
                reply["a"] = console.move2action(xy2move(human_xy.x, human_xy.y))
                console.prev_player = 2
                return reply 
        # return console.prompt("", batch)

    def actor(batch):
        return console.actor(batch)

    def train(batch):
        console.prompt("DF Train> ", batch)

    evaluator.setup(sampler=env["sampler"], mi=mi)

    GC.reg_callback_if_exists("actor_black", actor)
    GC.reg_callback_if_exists("human_actor", human_actor)
    GC.reg_callback_if_exists("train", train)

    GC.start()
    GC.GC.setRequest(
        mi["actor"].step, -1, env['game'].options.resign_thres, -1)

    evaluator.episode_start(0)

    while True:
        GC.run()
        if console.exit:
            break
    GC.stop()
