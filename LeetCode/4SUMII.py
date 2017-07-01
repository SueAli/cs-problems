from collections import defaultdict
class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        Time complexity is O(n^2)
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        r = 0
        A_B = defaultdict(int)

        for i in xrange(0,len(A)):
            for j in xrange (0, len(B)):
                A_B[A[i]+B[j]] += 1

        for k in xrange(0,len(C)):
            for l in xrange(0, len(D)):
                target = -1 * (C[k] + D[l])
                if target in A_B:
                    r +=  A_B[target]
        return r