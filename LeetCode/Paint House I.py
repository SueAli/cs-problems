# Paint House I

import sys

# Space Complexity is O(n)
# Time Complexit is O(n ) where n is the houses count
class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        cache = {}
        def findMincostRec(costs, h_idx , prev):

            if h_idx == len(costs):
                return 0
            if (h_idx, prev) in cache :
                return cache[(h_idx, prev)]

            min_cost = sys.maxint
            for c in range(len(costs[0])):
                if c != prev:
                    min_cost = min(min_cost, costs[h_idx][c] + findMincostRec(
                        costs, h_idx+1, c   ))
            cache[(h_idx, prev)] = min_cost
            return cache[(h_idx, prev)]

        return  findMincostRec(costs, 0 , None)
