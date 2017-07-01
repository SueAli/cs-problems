# Word Ladder II
#https://www.interviewbit.com/problems/word-ladder-ii/
from collections import deque
import string
class Solution:
    # @param start : string
    # @param end : string
    # @param dictV : list of strings
    # @return a list of list of strings
    def findLadders(self, start,end, dictV):

        def getNextTransf(curr,currPath,visited,q,dic_v):
            for i in range(len(curr)):
                for x in string.lowercase:
                    tmp = curr[:i]+x+curr[i+1:]
                    if tmp not in visited and tmp in dic_v:
                        q.append((tmp,currPath+[tmp]))

        dic_v = set(dictV)
        dic_v.add(end)
        q = deque()
        visited = set()
        q.append((start,[start]))
        res = []
        found = False
        while q:
            q_size = len(q)
            for i in range(q_size):
                currV,currPath = q.popleft()
                visited.add(currV)
                if currV == end:
                    res.append(currPath)
                    found = True
                if not found:
                    getNextTransf(currV,currPath,visited, q,dic_v)
            if found:
                break
        return res


s = Solution()
start = "hit"
end = "cog"
dict = ["hot","dot","dog","lot","log"]
print s.findLadders(start,end,dict)