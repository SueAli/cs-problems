

from collections import deque
# Time complexity is R * C as each grid will be visited once

while True:
  try:
    T = int(input())
    for t in range(T):
      R,C,M,N = map(int,input().split())

      W = int(input())
      grid = [[0 for c in range(C)] for r in range(R)] #0 means it is unvisited grid

      for w in range(W):
        w_r, w_c = map(int,input().split())
        grid[w_r][w_c] = -1 # Means it is a water grid
      # create a set with all possible movements using M, N
      # using set to avoid duplicates in case of :
      ### M = N
      ### M = 0 or N = 0
      directions = set([(M,N), (M,-N), (-M,N), (-M, -N), (N,M), (N,-M), (-N,M),(-N,-M)])

      # start from grid(0,0) I'm assuming that it will never contain water
      even_cnt = 0
      odd_cnt = 0

      q = deque()
      q.append((0,0))
      grid[0][0] = 1 # mark this grid as visited
      while q:
        curr_grid = q.popleft()
        cnt = 0  # represent total count of grids reachable from curr grid in one jump
        for d in directions:
          move_r , move_c = curr_grid[0] + d[0] , curr_grid[1]+d[1]
          if move_r < 0 or move_c < 0 or move_r >= R or move_c >= C or grid[move_r][move_c] == -1 :
            continue
          cnt += 1
          if not grid[move_r][move_c] :  # unvisited grid
            q.append((move_r,move_c))
            grid[move_r][move_c] = 1

        if cnt % 2 == 0:
          even_cnt += 1
        else:
          odd_cnt += 1

      print("Case "+ str(t+1)+ ":"+" "+str(even_cnt)+ " "+ str(odd_cnt))
  except:
    break



