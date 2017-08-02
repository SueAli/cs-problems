from collections import deque
import sys
class loc:
    def __init__(self,r,c,t,f):
        self.row = r
        self.col = c
        self.time = t
        self.facing = f

def isBlock(g, i, j, M,N):
    # if facing == 'south':
    #     if g[r][c-1] =='1' or g[r][c] == '1':
    #         return True
    #     return False
    # elif facing =='north':
    #     if g[r-1][c-1]=='1' or g[r-1][c] =='1':
    #         return True
    #     return  False
    # elif facing == 'west':
    #     if g[r-1][c-1]=='1' or g[r][c-1]== '1':
    #         return True
    #     return False
    # else:# east
    #     if g[r-1][c]=='1' or g[r][c] =='1':
    #         return  True
    #     return False
    if i < 1 or j < 1 or i > (N-1) or j > (M-1):
        return  True
    if (g[i][j] =='1'):
        return True;
    if ( g[i][j + 1] ):
        return True;
    if ( g[i + 1][j]):
        return True;
	if (g[i + 1][j + 1]):
            return True
    return False


while True:
    try:
        N,M = map(int,raw_input().split())
        if N == 0 and M == 0 :
            break
        grid = []
        bfs_q = deque()
        dir_words = ['s','n','w','e']
        dir_ = [(1,0),
                (-1,0),
                (0,-1),
                (0,1)]
        forward_steps = [1,2,3]
        loc_time = [[[sys.maxsize for d in range(4)] for mm in range(N)] for nn in range(M)]
        for i in range(N):
            grid.append(raw_input().split()) # 1 block , 0 Empty cell

        B1,B2,E1,E2,facing= raw_input().split()
        src_i,src_j,dst_i,dst_j = int(B1),int(B2), int(E1), int(E2)

        for i in range(4):
            if dir_words[i][0] == facing[0]:
                 loc_time[src_i][src_j][i] =0
                 bfs_q.append(loc(src_i,src_j,0,i))
                 break








        notFound = True
        level = 0
        while bfs_q:
                curr_loc = bfs_q.popleft()
                if curr_loc.row == dst_i and curr_loc.col == dst_j:
                    notFound = False
                    print(level)
                    break

                for step in forward_steps:
                    next_r = curr_loc.row + step* dir_[curr_loc.facing][0]
                    next_c = curr_loc.col + step* dir_[curr_loc.facing][1]
                    if  ( isBlock(grid,next_r,next_c,M,N)):
                        break

                    if loc_time[next_r][next_c][curr_loc.facing] < 1+loc_time[curr_loc.row][curr_loc.col][curr_loc.facing]:
                        continue

                    loc_time[next_r][next_c][curr_loc.facing]= curr_loc.time +1
                    bfs_q.append(loc(next_r,next_c,loc_time[next_r][next_c][curr_loc.facing],curr_loc.facing))


                for f in range(4):
                    if (f != curr_loc.facing
                        and loc_time[curr_loc.row][curr_loc.col][f] > 1+loc_time[curr_loc.row][curr_loc.col][curr_loc.facing] ):
                        loc_time[curr_loc.row][curr_loc.col][f] = 1+loc_time[curr_loc.row][curr_loc.col][curr_loc.facing]
                        bfs_q.append(loc(curr_loc.row,curr_loc.col,curr_loc.time,f))

        if notFound:
            print (-1)
    except :
        break