from collections import deque
class Solution(object):

    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        find connected component
        Time complexity is O( n * n)
        Space Complexity is O(n*n )

        """
        circles_cnt = 0
        n = len(M)
        visited = [False for _ in xrange(n)]

        def bfs(start):
            visited [start] = True
            q = deque()
            q.append(start)
            while q:
                curr_src = q.popleft()
                for j in range(n):
                    if M[curr_src][j] == 1 and not visited[j]:
                        visited[j] = True
                        q.append(j)

        for i in xrange(n):
            if not visited[i] :
                circles_cnt += 1
                bfs(i)

        return circles_cnt
