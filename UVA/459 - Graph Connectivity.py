from collections import deque
import sys
def bfs(edges_list, src, visited):
    q = deque()
    visited[src] = True
    q.append(src)
    while q:
        curr_u = q.popleft()
        for v in edges_list[curr_u]:
            if not visited[v]:
                visited[v] = True
                q.append(v)

def findConnectedGrap(edge_l, n):
    c_num = 0
    visited = [False for _ in range(n)]
    for i in range(n):
        if not visited[i]:
            c_num += 1
            bfs(edge_l, i , visited)
    return c_num



# Reading Input
t = int(input())
input()
for tt in range(t):
    n = input()
    n = ord(n)%64 # convert char to num  starting from 0
    #print(n)
    edges_list = [[] for _ in range(n)]
    for e in sys.stdin:
      e = e.rstrip()
      if not e:
        break
      u,v = ord(e[0])%64 , ord(e[1])%64
      edges_list[u-1].append(v-1)
      edges_list[v-1].append(u-1)

    print (findConnectedGrap(edges_list,n))
    if tt != t-1:
        print ("")


