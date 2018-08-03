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


class Game(object):
    def __init__(self, stub, console):

        self.prev_player = 0

        self.res_len = 0

        self.color = {'has_chosen': False, "client": 1, "AI": 2}

        self.stub = stub

        self.console = console

    
    def __call__(self):
        
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

if __name__ == '__main__':
    address = addrs['game_server']
    if address != "":
        channel = grpc.insecure_channel(address + ':50051')
    else :
        channel = grpc.insecure_channel("localhost:50051")
    stub = play_pb2_grpc.TurnStub(channel)
    