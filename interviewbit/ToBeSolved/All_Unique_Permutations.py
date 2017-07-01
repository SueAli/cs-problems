class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def permute(self, A):
        res=[]
        list.sort(A)
        def permute(a, l, r,res):
            if l==r:
                res.append(a[:])
            else:
                for i in xrange(l,r+1):
                    if i != l and a[i] == a[i-1]:
                        continue
                    a[l], a[i] = a[i], a[l]
                    permute(a, l+1, r,res)
                    a[l], a[i] = a[i], a[l]
        permute(A,0,len(A)-1,res)
        return res

s = Solution()
print s.permute([ 0, 0, 0, 1, 9 ])


