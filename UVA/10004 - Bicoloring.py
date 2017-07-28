#  10004 - Bicoloring - UVA
# python 3.5.x

from collections import deque
while True:
      n = int(input())
      if n == 0:
        break
      colored = [ 0 for _ in range(n)]
      adj_list = [[0 for mm in range(n)] for _ in range(n)]
      l = int(input())
      for i in range(l):
        u,v = map(int,input().split())
        adj_list[u][v] = 1
        adj_list[v][u] = 1
      q = deque()
      res = "BICOLORABLE."
      q.append(0)
      colored[0] = 1
      while q:
        curr_node = q.popleft()
        for neighbor in range(n):# len(adj_list[curr_node]):
          if adj_list[curr_node][neighbor] == 1 and colored[neighbor] == 0:
            colored[neighbor] = -1 * colored[curr_node]
            q.append(neighbor)

          elif adj_list[curr_node][neighbor]  == 1 and colored[neighbor] ==colored[curr_node]:
            res = "NOT BICOLORABLE."
            break

      print (res)



