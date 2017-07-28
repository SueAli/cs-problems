import sys
from collections import defaultdict
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [ amount+1 for x in xrange( amount +1 )]
        dp[0] = 0
        for c in coins :
            for i in xrange(c,amount +1 ):
                    dp [ i ] = min(dp[i-c] + 1 , dp[i])

        if dp[amount] > amount:
            return -1
        return  dp[amount]


