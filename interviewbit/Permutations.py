class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def permute(self, A):
        import copy
        def perm(n, i,pe):
           # print "i", i ,"____________"
            #print n
            if i == len(n) - 1:
                t = copy.copy(n)
                pe+= [t]
            else:
                for j in range(i, len(n)):
                    n[i], n[j] = n[j], n[i]
                    perm(n, i + 1,pe)
                    n[i], n[j] = n[j], n[i] # swap back, for the next loop
            return pe
        return perm(A,0,[])

s = Solution()
print s.permute([1,3,4])