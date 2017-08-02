#   924 - Spreading The News
from collections import deque

def bfs(src_,adj_list_,e):
    # Time Complexity is O(E+V)
    q = deque()
    visited = [False for _ in range(e)]
    q.append(src_)
    visited[src_] = True
    max_boom_size = 0
    first_day = 0
    curr_day_id = 0
    while q:
        curr_day_id += 1
        curr_len = len(q)
        today_broadcast = 0
        for _ in range(curr_len):
            curr_emp = q.popleft()
            for v in adj_list_[curr_emp]:
                if not visited[v]:
                    today_broadcast += 1
                    visited[v] = True
                    q.append(v)
        if today_broadcast > max_boom_size:
            max_boom_size = today_broadcast
            first_day = curr_day_id

    return max_boom_size, first_day
while True:
    try:
        E = int(input())
        if E == 0 :
            break
        adj_list =[]
        for i in range(E):
            l = [int(x) for x in input().split()]
            if l[0] > 0 :
                adj_list.append(l[1:])
            else:
                adj_list.append([])

        t = int(input())
        while t > 0 :
            src = int(input())

            boom_size,_1st_day = bfs(src,adj_list,E)

            if boom_size == 0:
                print ('0')
            else:
                print (boom_size,_1st_day)
            t -= 1
    except:
        break