#Knight movement on a chess board
# https://www.interviewbit.com/problems/knight-on-chess-board/
from collections import deque
class Solution:
   # @param N : integer
   # @param M : integer
   # @param x1 : integer
   # @param y1 : integer
   # @param x2 : integer
   # @param y2 : integer
   # @return an integer
   def knight(self, N, M, x1, y1, x2, y2):
       #Time Complexity is O(N*M)
       #Space Complexity is O(N*M)
       def getNeigbors(x,y):
           q = set()
           q.add((x-2,y-1))
           q.add((x-2,y+1))
           q.add((x-1,y+2))
           q.add((x+1,y+2))
           q.add((x+2,y-1))
           q.add((x+2,y+1))
           q.add((x-1,y-2))
           q.add((x+1,y-2))
           return q
       if x1 == x2 and y1==y2: return 0
       paths = {(x1-1,y1-1):1}
       q = deque()
       v = set()
       q.append((x1-1,y1-1))
       while q:
            v_x,v_y = q.popleft()
            if (v_x,v_y) in v:
                continue
            v.add((v_x,v_y))
            for next in getNeigbors(v_x,v_y):
               if 0 <= next[0] < N and 0<= next[1] < M :
                    if next[0] == x2-1 and next[1] == y2-1:
                       return paths[(v_x,v_y)]
                    else:
                        q.append(next)
                        paths[next] = paths[(v_x,v_y)]+1
            del paths[(v_x,v_y)]
       return -1



