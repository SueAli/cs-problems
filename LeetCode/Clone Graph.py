# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

from collections import deque
class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        # timec complexity is O(n)
        # Space complexity is O(n)
        new_node = None
        q = deque()
        if not node:
            return node
        edges = set()
        nodes_ht = {}
        q.append(node)
        new_node = None
        while q :
            curr_node = q.pop()
            if curr_node.label not in nodes_ht:
                nodes_ht[curr_node.label] = UndirectedGraphNode(curr_node.label)
                # set for neigbors
            for n in curr_node.neighbors :
                if n.label not in nodes_ht:
                    nodes_ht[n.label] = UndirectedGraphNode(n.label)
                    q.append(n)
                nodes_ht[curr_node.label].neighbors.append(nodes_ht[n.label])

            if not new_node :
                new_node = nodes_ht[curr_node.label]

        return new_node