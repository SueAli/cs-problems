# Predict the Winner
class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        Time Complexity is O( n * n )
        Space Complexity is O ( n * n ) for dp table
        """
        mem = {}
        def winner(nums,s,e):
            if s == e:
                return nums[s]
            if (s,e) not in mem:
                a =  nums[s] - winner(nums,s+1,e)
                b =  nums[e] - winner(nums,s,e-1)
            	mem[(s,e)] = max(a, b)
            return mem[(s,e)]
        return winner(nums,0,len(nums) - 1) >= 0
