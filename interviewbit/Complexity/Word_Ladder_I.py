# https://www.interviewbit.com/problems/word-ladder-i/
# Word Ladder I
from collections import deque
import string
class Solution:
    # @param start : string
    # @param end : string
    # @param dictV : list of strings
    # @return an integer
    def ladderLength(self, start, end, dictV):
        def getNextTransf(curr,end, currTrans,q,dic_v):
            if curr == end:
                return True
            for i in range(0,len(curr)):
                for x in list(string.ascii_lowercase):
                    tmp = curr[0:i]+x+curr[i+1:]
                    if tmp not in currTrans and tmp in dic_v:
                        q.append(tmp)
                        currTrans[tmp] = currTrans[curr]+1
            return False


        dic_v = set(dictV)
        currTrans = {start:1}
        q= deque()
        q.append(start)
        while q:
            l = len(q)
            for i in range(l):
                curr = q.popleft()
                flag = getNextTransf(curr,end, currTrans,q,dic_v)
                if flag:
                    return currTrans[end]
        return 0
