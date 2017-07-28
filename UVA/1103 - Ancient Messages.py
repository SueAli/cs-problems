
from collections import deque
#Time Complexity is h * w


def findConnectedComp(r_st,r_end,c_st,c_end,R,C,c1,c2,image):
    white_comp_cnt = 0
    for i in range(r_st,r_end+1):
        for j in range(c_st,c_end+1):
            if image[i][j] == c1:
                white_comp_cnt += 1
                floodFill(i,j,R,C,c1,c2,image)
    return white_comp_cnt

def floodFill(r,c,R,C,c1, c2, image):
    _dir = [(0,-1),(1,0),(-1,0),(0,1)]#,(-1,-1),(-1,1),(1,1),(1,-1)]
    q = deque()
    q.append((r,c))
    while q:
      p_r, p_c = q.popleft()
      image[p_r][p_c] = c2
      for d in _dir:
        new_r , new_c = p_r + d[0], p_c + d[1]
        if not ( new_r< 0 or new_c < 0 or new_r >= R or new_c >= C or image[new_r][new_c] != c1):
          image[new_r][new_c] = c2
          q.append((new_r,new_c))

def findWhiteComponentShape(r,c,R,C,c1, c2, image):
    _dir = [(0,-1),(1,0),(-1,0),(0,1)]#,(-1,-1),(-1,1),(1,1),(1,-1)]
    white_comp = 0
    q = deque()
    q.append((r,c))
    while q :
      p_r, p_c = q.popleft()
      image[p_r][p_c] = c2
      for d in _dir:
        new_r , new_c = p_r + d[0], p_c + d[1]
        if new_r< 0 or new_c < 0 or new_r >= R or new_c >= C or image[new_r][new_c] == -1:
          continue
        elif image[new_r][new_c] == 0 : # white component
          white_comp += 1
          floodFill(new_r,new_c,R,C,0,-1,image)
        else :
          image[new_r][new_c] = c2
          q.append((new_r,new_c))
    return white_comp




def main_fn(image, h, w):

    # color background into any other color num = #
    letters_white_comp= {1:'A', 3:'J',5:'D',4:'S',0:'W', 2:'K'}
    found = []

    for i in [0,h-1]:
        for j in range(0,w):
            if image[i][j] == 0:
                floodFill(i,j,h,w,0,-1 , image)

    for j in [0,w-1]:
        for i in range(0,h):
            if image[i][j] == 0:
                floodFill(i,j,h,w,0,-1 , image)


    # start finding shapes colored in black  and then find the number of connected component inside

    for i in range(h):
        for j in range(w):
            if image[i][j] == 1: # black shape
                # Recolor black pixels into -1 and find the borders of it
                # for l in image:
                #   print (l)

                # find white components inside this shape
                conn_comp = findWhiteComponentShape(i,j,h,w,1,-1, image)
                # Map it to the letter

                if conn_comp in letters_white_comp:
                    found.append(letters_white_comp[conn_comp])

    found.sort()
    found_word = "".join(found)
    return found_word




# Reading input
t = 1
while True:
    H,W = map(int, input().split())
    if H == 0  and W == 0 :
        break

    line_width = 4*W
    grid = []
    for i in range(H):
        l_bin = bin(int(input(),16))[2:]
        l_ = l_bin.zfill(line_width)
        grid.append([int(c) for c in l_ ])

    shapes = main_fn(grid,H,line_width)
    print ("Case "+str(t)+": "+shapes)
    t += 1
