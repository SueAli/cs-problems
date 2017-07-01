# Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ## Time Complexity is O(n)
        ## Space Complexity is O(1)
        max_profit = 0
        buy_idx = 0
        for i in xrange(1,len(prices)):
            tmp = prices[i] - prices[buy_idx]
            if tmp > max_profit:
                max_profit = tmp
            elif prices[i] < prices[buy_idx]:
                buy_idx = i
        return max_profit



