from collections import deque
def maxContinentsDFS( r,c,m,n, grid,visited, king_char,max_s):
    dir_= [(0,-1),(0,1),(-1,0),(1,0)]

    if(c<0) :
      c=n-1;

    if(c>=n) :
      c=0;

    if(r<0 or r>=m) or  grid[r][c] != king_char  :
        return;

    grid[r][c] = '!'
    max_s[0] += 1
    for d in dir_:
        new_r , new_c = r +d[0], c + d[1]
        maxContinentsDFS(new_r,new_c,m,n,grid,visited,king_char,max_s)

    return



while True:
    try:
        m,n = map(int,input().split())
        if m == 0  and n == 0 :
            break
        map_ = []
        visit_flag = [[False for nn in range(n)] for mm in range(m)]
        for i in range(m):
            l = str(input().strip())
            map_.append([c for c in l])
        x_y = input().split()
        x,y = int(x_y[0]), int(x_y[1])


        king_char = map_[x][y]


        maxContinentsDFS(x,y,m,n,map_,visit_flag,king_char,[0])
        max_land_size = 0
        for rr in range(m):
          for cc in range(n):
            if  map_[rr][cc] == king_char:
              tmp = [0]
              maxContinentsDFS(rr,cc,m,n,map_,visit_flag,king_char,tmp)
              max_land_size = max(max_land_size,tmp[0] )

        print (max_land_size)
        input()
    except:
      break
