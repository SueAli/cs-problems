# 929 Number Maze
import sys
from sys import stdin
import heapq

class edge:
    def __init__(self,cost,dst_row,dst_col):
        self.weight = cost
        self.row = dst_row
        self.col = dst_col
    def __lt__(self, other):
        return self.weight < other.weight
dir_ = [(1,0),(-1,0),(0,1),(0,-1)]
while True:
  try:
    T = int(input())
    for tt in range(T):
        n = int(input())
        m = int(input())
        maze = []
        dist_cost =[[sys.maxsize for cc in range(m)] for rr in range(n)]
        min_heap = []

        for i in range(n):
            ll = sys.stdin.readline()
            l = [ord(ll[x])-48 for x in range(2*m-1) if ll[x].isdigit()]
            maze.append(l)
        dist_cost[0][0] = maze[0][0]
        heapq.heappush(min_heap,edge(dist_cost[0][0],0,0))

        while min_heap:
            curr_cell = heapq.heappop(min_heap)
            for d in dir_:
                new_i, new_j = curr_cell.row+d[0], curr_cell.col+d[1]
                if new_i <0 or new_i == n or new_j <0 or new_j == m:
                    continue
                if ((dist_cost[curr_cell.row][curr_cell.col] +
                         maze[new_i][new_j]) < dist_cost[new_i][new_j]):
                    dist_cost[new_i][new_j] = dist_cost[curr_cell.row][curr_cell.col]+ maze[new_i][new_j]
                    heapq.heappush(min_heap,edge(dist_cost[new_i][new_j],new_i,new_j))

        print( dist_cost[n-1][m-1])

  except:
    break


