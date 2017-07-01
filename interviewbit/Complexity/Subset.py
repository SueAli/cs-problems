#Given a set of distinct integers, S, return all possible subsets.
# Example :
#
# If S = [1,2,3], a solution is:
#
# [
#   [],
#   [1],
#   [1, 2],
#   [1, 2, 3],
#   [1, 3],
#   [2],
#   [2, 3],
#   [3],
# ]
class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    ## Time Complexity is O( n ^ 2)
    ## Space complexity is O ( n ^ 2)
    def getSubsetRec(self, arr, curr_set, rem_start, rem_end, res):
        res.append(curr_set[:])
        if rem_start > rem_end:
            return
        for d in range(rem_start, rem_end +1 ):
            curr_set.append(arr[d])
            self.getSubsetRec(arr,curr_set,d+1,rem_end,res)
            curr_set.pop()

    def subsets(self, A):
        A.sort() # O( nlog n)
        result =[]
        curr = []
        self.getSubsetRec(A,curr,0,len(A) - 1, result)
        return result

