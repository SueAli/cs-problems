import sys
from collections import deque
dir_ = [(0,-1),(0,1),(-1,0),(1,0)]
while True:
  try:
    R,C = map(int,input().split())
    if R == 0 and C == 0 :
      break
    dist = [[sys.maxsize for _ in range(C)] for x in range(R)]
    map_ = [[1 for _ in range(C)] for x in range(R)] # 1 : is Ok , 0 is bomb

    b_rows= int(input())
    for _ in range(b_rows):
      cols = list(map(int,input().split()))
      row_id = cols[0]
      for c_id in range(1,len(cols)):
        map_[row_id][cols[c_id]] = 0


    src_r, src_c = map(int, input().split())
    dst_r, dst_c = map(int, input().split())
    dist[src_r][src_c] = 0
    q = deque()
    q.append((src_r,src_c))
    sol_fnd = False
    while q :
      if sol_fnd:
        break
      u_r, u_c = q.popleft()

      for d in dir_:
        v_r, v_c = u_r+d[0], u_c + d[1]
        if (v_r <0 or v_c < 0 or v_r == R or v_c == C or map_[v_r][v_c] == 0 or
        dist[v_r][v_c] != sys.maxsize):
          continue

        dist[v_r][v_c] = dist[u_r][u_c] +1
        if v_r == dst_r and v_c == dst_c:
          sol_fnd = True
          break
        q.append((v_r,v_c))

    print( dist[dst_r][dst_c])


    #src_r, src_c = map(int, input())

  except:
    break