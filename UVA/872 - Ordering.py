#  872 - Ordering

# The main idea is that any possible topolgical sorting starts wit
# node with (indegree == 0) --> it can be applied recursively to find all
# possible topological sorting

def recToplogicalSort(n,indegree_,visited_,adj_,partial_res,final_res,nodes ):
  adj_found = False
  for i in range(n):
    if indegree_[i] == 0 and not visited_[i]:

      # delete all outgoing edges from this node to all its adj nodes
      for v in adj_[i]:
        indegree_[v] -= 1
      # add this node to the result # add the actual letter
      partial_res.append(nodes[i])
      visited_[i] = True
      # Recursivly look for the next node
      recToplogicalSort(n,indegree_,visited_,adj_,partial_res,final_res,nodes )
      # After returning from the recursive call , u should re-add the deleted edge
      for v in adj_[i]:
        indegree_[v] += 1
      visited_[i] = False
      partial_res.pop()
      adj_found = True

  if not adj_found: # No more nodes to explore
    final_res.append(partial_res[:])





while True:
    try:
      t = int(input())
      input()
      for tt in range(t):
        nodes = input().split()
        nodes_dic = dict()
        for i in range(len(nodes)):
          nodes_dic[nodes[i]] = i
        n = len(nodes)
        visited = [False for _ in range(n)]
        adj_list= [[] for _ in range(n)]
        indegree = [0 for _ in range(n)]

        relations = input().split()

        for r in relations:
          adj_list[nodes_dic[r[0]]].append(nodes_dic[r[2]])
          indegree[nodes_dic[r[2]]] += 1
        final_res = []
        # call for topological sorting
        recToplogicalSort(n,indegree,visited,adj_list,[],final_res,nodes )

        if len(final_res) > 0 and len(final_res[0]) == n :
          for ff in final_res:
            print(" ".join(ff))
        else:
          print("NO")
        if tt < t-1:
          print("")
        # Read the empty line after this case
        input()

    except:
        break


