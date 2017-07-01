# Bulbs
# https://www.interviewbit.com/problems/bulbs/
class Solution:
    # @param A : list of integers
    # @return an integer
    def bulbs(self, A):
        ##  Time Complexity is O(n)
        ##  Space Complexity is O(1)
        clicks, i , key = 0 , 0 , 0
        while i < len(A):
            if A[i] == key:
                clicks += 1
                key = key ^ 1
            i += 1
        return clicks


