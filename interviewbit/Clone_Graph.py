# Clone Graph
#https://www.interviewbit.com/problems/clone-graph/

# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
from collections import deque
class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        visited = {}
        new_node = None
        q = deque()
        q.append(node)
        while q:
            curr = q.popleft()
            if curr not in visited:
                tmp = UndirectedGraphNode(curr.label)
                visited[curr] = tmp
                if len(visited) ==1:
                    new_node = visited[curr]
            else:
                continue
            if curr.neighbors:
                q.extend(curr.neighbors)

        for item in visited:
            for c in item.neighbors:
                visited[item].neighbors.append(visited[c])
        return new_node


