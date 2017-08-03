# 10801 Lift Hopping
import sys
from heapq import  heappush, heappop

class floor :
    def __init__(self,t,l, e):
        self.reached_  = t
        self.floor_num = l
        self.elevator = e
    def __lt__(self, other):
        return self.reached_ < other.reached_


while True:
    try:

        n,k = map(int, input().split())
        elevators_time =list( map(int,input().split()))

        elevators_to_floor = [[0 for c in range(100)] for r in range(n)]
        for i in range(n):
            l = list(map(int,input().split()))
            for f in l:
                elevators_to_floor[i][f] = 1

        switch_time = 60 # 1 min

        floors_time = [sys.maxsize for _ in range(100)]


        floors_queue = []
        floors_time[0] = 0 #  to achieve start floor it takes 0 time

        notFound  = True

        heappush(floors_queue,floor(0,0,None))
        while floors_queue:
            dst_f = floors_queue.pop()

            for e in range(n):
                if elevators_to_floor[e][dst_f.floor_num] == 1: # this elevator is

                    for f in  range(len(elevators_to_floor[e])):
                        if elevators_to_floor[e][f] == 1:
                            tmp_time = dst_f.reached_
                            #if not dst_f.elevator or dst_f.elevator == e:
                            tmp_time += abs(dst_f.floor_num - f ) * elevators_time[e]

                            if dst_f.elevator is not None and dst_f.elevator != e: # I need to switch
                                tmp_time += switch_time

                            if tmp_time < floors_time[f] :
                                floors_time[f] = tmp_time

                                heappush(floors_queue,floor(tmp_time,f,e))


        if floors_time[k] != sys.maxsize :
          print (floors_time[k])
        else:
            print("IMPOSSIBLE")
    except:
        break