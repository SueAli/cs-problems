#  11060 - Beverages - UVA
# python 3.5.1
def toplogicalSortDFS(n,visited, adj, s,bev_names,in_deg):
  for v in range(n):
    if in_deg[v] == 0 and not visited[v]:
      visited[v] = True
      s.append(bev_names[v])
      for x in adj_list[v]:
        in_deg[x] -= 1
      toplogicalSortDFS(n,visited, adj, s,bev_names,in_deg)


t = 0
while True:
    try:
      t += 1
      n = int(input())
      bev_dict={}
      bev_list=[]
      for i in range(n):
        b = input()
        bev_dict[b] = i
        bev_list.append(b)
      r_cnt = int(input())
      adj_list = [[] for _ in range(n)]
      visited = [False for _ in range(n)]
      in_degree= [0 for _ in range(n)]
      for r in range(r_cnt):
        curr_r = input().split()
        adj_list[bev_dict[curr_r[0]]].append( bev_dict[curr_r[1]])
        in_degree[bev_dict[curr_r[1]]] += 1

      res = []
      toplogicalSortDFS(n, visited,adj_list,res,bev_list, in_degree)


      print("Case #"+str(t)+": Dilbert should drink beverages in this order: "+
      " ".join(res)+".")
      print ()
      # Read blank line
      input()

    except:
        break


