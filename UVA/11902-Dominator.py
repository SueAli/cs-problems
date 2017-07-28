from collections import  deque
# 11902 UVA  Dominator
# Time Complexity V * V *V
def dfs(src,adj_mat,visited):
    visited[src] = True
    for i in range(len(adj_mat[0])):
        if adj_mat[src][i] == 1 and not visited[i]:
            dfs(i,adj_mat,visited)

def bfs(src, adj_mat, visited):
    visited[src] = True
    q = deque()
    q.append(src)
    while q:
        curr_v = q.popleft()
        for i in range(len(adj_mat[0])):
            if not visited[i]  and adj_mat[curr_v][i] == 1:
                visited[i] = True
                q.append(i)


def formatOutput(res,n):
        f_res = []
        for r in range(len(res)):
            if r ==0 :
                f_res.append('+'+("".join(['-' for _ in range(2*n-1)]))+'+')
                #print ('+'+("".join(['-' for _ in range(2*n-1)]))+'+')
            tmp =[]
            for c in range(len(res[0])):

                if c ==0:
                    tmp .append( "|")
                tmp.append( res[r][c])
                tmp .append( "|")
            f_res.append ("".join(tmp))
            f_res.append('+'+("".join(['-' for _ in range(2*n-1)]))+'+')
        return f_res

def findDmon(adj_matrix,n):
    dmo_output = [['X' for _ in range(n)] for _ in range(n)]
    for i in range(0,n):
        visited = [False for _  in range(n)]
        if i == 0 :
            dfs(0,adj_matrix,visited)
        else:
            visited[i] = True # To ignore dmoniator
            dfs(0,adj_matrix, visited)
        for j in range(n):
            if i != 0 and j == i :
              dmo_output[i][j] = 'Y' if dmo_output[0][j]=='Y' else 'N'
            elif i == 0:
                dmo_output[i][j] = 'Y' if visited[j] else 'N'
            else:
                dmo_output[i][j] = 'Y' if (dmo_output[0][j]=='Y'
                                           and not visited[j]) else 'N'

    res = formatOutput(dmo_output,n)
    for r in res:
        print (r)

# t  = int(input())
# tests =[]
# for x in range(1,t+1):
#             mat = []
#             n= int(input())
#             for rr in range(n):
#                 m = input()
#                 l = list(map(int,m.split()))
#                 mat.append(l)
#             tests.append((mat,n))
# for tt in range(1,t+1):
#             print("Case {:,}:".format(tt))
#             findDmon(tests[tt-1][0],tests[tt-1][1])
while True:
    try:
        t  = int(input())
        tests =[]
        for x in range(1,t+1):
            mat = []
            n= int(input())
            for rr in range(n):
                m = input()
                l = list(map(int,m.split()))
                mat.append(l)
            tests.append((mat,n))
        for tt in range(1,t+1):
            print("Case {:,}:".format(tt))
            findDmon(tests[tt-1][0],tests[tt-1][1])

    except:
        break





