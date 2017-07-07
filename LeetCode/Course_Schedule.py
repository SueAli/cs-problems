
class Solution(object):

    def DFSTraverse(self,g, v, visited):
        if visited[v] == -1: # This node is visited before in the current cycle
            return False

        if visited[v] == 1: # this node has been visited before and no cycles found starting traversing from it
            return True
        else:
            visited[v] = -1 # mark this node as visited in the current cycle
            for m in g[v]:
                if not self.DFSTraverse(g, m, visited):
                    return False
            visited[v]= 1 # done visiting from starting node and no cycles found
            return True

    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        # Depth first Search
        Time complexity is O( V + E  ) where v is the  numCourses and E  is the len (prerequisites)
        Space Compexity is O(V) for recusive functions call
        Course Schedule
        """
        if numCourses > 1 :
            g = [[] for x in xrange(numCourses)]
            for e in prerequisites:
                g[e[0]].append(e[1])

            visited = [ 0 for x in xrange(numCourses)]
            for i in xrange(numCourses) :
                if not self.DFSTraverse(g, i, visited):
                    return False
        return True
