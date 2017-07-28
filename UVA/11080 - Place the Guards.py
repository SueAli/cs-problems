# 11080 - Place the Guards - UVA
from collections import deque
def checkBiParatite(src,n, adj_mat, color):
  biparatite_flag = True
  q=deque()
  color[src] = 0
  zero_set_cnt = 0
  total_traversed = 0
  q.append(src)
  while q:
    curr_node = q.popleft()
    if color[curr_node] == 0:
      zero_set_cnt += 1
    total_traversed += 1
    for v in range(n):
      if color[v]== -1  and adj_mat[curr_node][v] == 1:
        color[v] = 1 - color[curr_node]
        q.append(v)

      elif adj_mat[curr_node][v] == 1 and color[v] == color[curr_node]:
        biparatite_flag = False
        break
  if biparatite_flag:
    if total_traversed == zero_set_cnt:
      return zero_set_cnt
    return min(zero_set_cnt,total_traversed - zero_set_cnt)
  else:
    return -1

T = int(input())
while True:
  try:
    for t in range(T):
      n,l = map(int,input().split())
      adj_matrix = [[0 for _ in range(n)] for x in range(n)]
      color = [-1 for _ in range(n)]
      visited = [False for _ in range(n)]
      for _ in range(l):
        u,v = map(int,input().split())
        adj_matrix[u][v] = 1
        adj_matrix[v][u] = 1
      guards_cnt = 0
      sol_found = True
      for x in range(n):
        if color[x] == -1 : # not visited yet
          tmp = checkBiParatite(x,n,adj_matrix,color)
          if tmp == -1 :
            sol_found = False
            break
          else:
            guards_cnt += tmp
      if sol_found:
        print(guards_cnt)
      else:
        print(-1)
  except:
    break






      