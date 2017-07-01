# Highest Product
# https://www.interviewbit.com/problems/highest-product/
class Solution:
    # @param A : list of integers
    # @return an integer
    ## Time Complexity is O( n log n )
    ## Space Complexity is O(1)
    def maxp3(self, A):
        n = len(A)
        A.sort()
        if n < 3:
            return 0
        m1,m2,m3 = A[-1],A[-2],A[-3]
        max_product = m1 * m2 * m3
        if A[0] < 0 and A[1] < 0:
            tmp = A[0] * A[1] * m1
            if tmp > max_product:
                max_product = tmp
        return max_product

