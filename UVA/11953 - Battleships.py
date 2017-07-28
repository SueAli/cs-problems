# Time Complexity is O( n * n )
# Space Complexity is O( n * n )

dir_ = [(0,-1),(0,1),(-1,0),(1,0)]

def dfsFloodFill(i,j,grid, x_cnt):
    if (i <0 or j <0
        ) or (i == len(grid)
                     or j == len(grid[0])
                     or grid[i][j]=='.' or
                             grid[i][j] == '#' ):
        return
    if grid[i][j] == 'x':
        x_cnt[0] += 1

    grid[i][j] = '#'
    for d in dir_:
        dfsFloodFill(i+d[0],j+d[1],grid, x_cnt)

while True:
    try:
        T = int(input())
        for t in range(T):
            n = int(input())
            g = []
            for r in range(n):
                g.append(list(str(input())))

            ships_cnt = 0
            for ii in range(n):
                for jj in range(n):
                    if g[ii][jj] in ['x','@']:
                        x_cnt = [0]
                        dfsFloodFill(ii,jj,g, x_cnt)
                        if x_cnt[0] >0:
                            ships_cnt += 1

            print ("Case "+str(t+1)+": "+str(ships_cnt))
    except:
        break



