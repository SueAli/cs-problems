


# Time complexity is v * ( v + E)

# find cycles in directed graph

def dfs_tarjan(u,dfs_low,dfs_num, visited, s,curr_traverse_id,parent, nums_scc, cache, forward_depth):

    dfs_low[u], dfs_num[u] = curr_traverse_id,curr_traverse_id
    visited[u] = True
    s.append(u)
    forward_depth_bef = forward_depth[0]
    forward_depth[0] += 1
    if forwards_cnt[parent[u]] != -1 :
        forward_depth[0] += forwards_cnt[parent[u]]
    else:
        if dfs_num[parent[u]] == -1 :
            dfs_tarjan(parent[u], dfs_low,dfs_num,visited,s,curr_traverse_id+1,parent,nums_scc, cache,forward_depth)

        if visited[parent[u]]:
            dfs_low[u] = min(dfs_low[u],dfs_low[parent[u]])

    curr_cycle_len = forward_depth[0] - forward_depth_bef

    if dfs_low[u] == dfs_num[u] : # u is a start of cycle
        #print (curr_cycle_len)
        nums_scc[0] += 1
        #print  ("Cycle :"+str(nums_scc[0]))
        while True:
            m = s.pop()
            forwards_cnt[m] = curr_cycle_len
           # print  ("vertext: "+ str(v))
            if m == u : # end of current cycle
                break

while True:
  try:
      T = int(input())
      for t in range(T):
        n = int(input())
        parent = [ -1 for _ in range(n+1)] # adj array, as each v can forward for only one u vertex
        dfs_num = [-1 for _ in range(n+1)] # the first traverse id
        dfs_low = [-1 for _ in range(n+1)] # the lowest traverse id
                                        # reachable from this node
        visited = [False for _ in range(n+1)]
        forwards_cnt = [-1 for _ in range(n +1)] # cache the calc forward cnt for each node
        for _ in range(n):
          u,v = map(int, raw_input().split())
          parent[u] = v

        iteration_id = 0
        nums_scc = [0]
        max_f = -1
        start_node = -1
        s_stack = []
        # Main function

        for i in range(1,n+1):
            if forwards_cnt[i] == -1:
                dfs_tarjan(i,dfs_low,dfs_num,visited,[],iteration_id,parent,nums_scc,forwards_cnt,[0])
            if forwards_cnt[i] > max_f:
                max_f = forwards_cnt[i]
                start_node = i
        print("Case "+ str(t+1)+ ":"+" "+str(start_node))
        if t != T-1:
            print ("")

  except :
    break






