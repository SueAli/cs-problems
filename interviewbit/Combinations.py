import copy
class Solution:
    # @param n : integer
    # @param k : integer
    # @return a list of list of integers
    def combine(self, n, k):
        tmpList = [x for x in range(1,n+1)]
        finalList = []
        def finComb (a, start, currComb,k):
            if len(currComb) == k or start >= len(a):
                finalList.append(copy.copy(currComb))
                #print currComb
                return
            for i in range(start+1, len(a)):
                currComb.append(a[i])
                finComb(a,i, currComb,k)
                if len(currComb) > 0:
                    currComb.pop()
        finComb(tmpList,-1,[],k)
        return finalList

s = Solution()
print  s.combine(2, 1)