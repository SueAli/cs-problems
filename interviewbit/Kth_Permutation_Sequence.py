# Kth Permutation Sequence
# https://www.interviewbit.com/problems/kth-permutation-sequence/#

import math
class Solution:
    # @param n : integer
    # @param k : integer
    # @return a strings
    ## Time Complexity is O(n ^2)
    ## Space Complexity is O(n)
    def getPermutation(self, n, k):
        A = [str(i) for i in range(1,n+1)]
        k = k - 1 #0 based index
        start = 0
        res = []
        if k == 0:
            return "".join(A)
        while len(res) < len(A):
            curr_index = k/math.factorial(n-1)
            res.append(A[start+curr_index])
            self.shiftToRight(A,start,start+curr_index)
            k = k - curr_index * math.factorial(n-1)
            start += 1
            n -= 1
        return "".join(res)


    def shiftToRight(self,arr,st, end):
        tmp = arr[end]
        while end > st:
            arr[end] = arr[end-1]
            end -= 1
        arr[st] = tmp
