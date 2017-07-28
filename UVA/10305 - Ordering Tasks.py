#  10305 - Ordering Tasks - UVA
def topologicalSort(u,adj_list,marked,s):
    marked[u] = True
    for v in adj_list[u]:
      if not visited[v]:
        topologicalSort(v,adj_list,marked,s)
    s.append(u)


while True:
    try:
        n,m = map(int,input().split())
        if n == 0 and m == 0:
            break
        edge_list = [[] for _ in range(n+1)]

        for x in range(m):
            i,j = map(int, input().split())

            edge_list[i].append(j)



        visited = [False for _ in range(n+1)]
        s_stack= []
        for t in range(1,n+1):
            if not visited[t]:
                topologicalSort(t,edge_list,visited,s_stack)

        s_stack.reverse()


        print(" ".join(str(e) for e in s_stack))


    except:
        break


