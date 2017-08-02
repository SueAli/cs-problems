# https://uva.onlinejudge.org/external/11/1112.pdf
# Mice and Maze
import heapq
import sys
class edge:
  def __init__(self,c,end):
    self.cost = c
    self.end = end

  def __lt__(self,other):
    return self.cost < other.cost

while True:
  try:
    t = int(input())
    input()
    for tt in range(t):
      N = int(input())
      E = int(input())
      T = int(input())
      M = int(input()) # connections

      reached_exit = 0

      to_go_cost =[[] for _ in range(N)]
      min_heap = []
      cell_cost = [sys.maxsize for nn in range(N)]
      for mm in range(M):

        a,b, cost = input().split()
        to_go_cost[int(b)-1].append((int(cost), int(a)-1))

      cell_cost[E-1] = 0

      heapq.heappush(min_heap, edge(0,E-1))

      while min_heap:
        curr_edge = heapq.heappop(min_heap)
        if curr_edge.cost <= T :
          reached_exit += 1

        for v_time, v_dst in to_go_cost[curr_edge.end]:
          if curr_edge.cost+v_time < cell_cost[v_dst]:
            cell_cost[v_dst] = curr_edge.cost+v_time
            heapq.heappush(min_heap,edge(cell_cost[v_dst],v_dst))
      print(reached_exit)
      if tt < t - 1:
        print()
        input()
  except:
    break