class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # Time complexity is O(n)
        # Space complexity is O(1)
        max_prof = 0
        n = len(prices)
        if n > 1:
            paid = prices[0]
            for p in range(1,n):
                if prices[p] - paid > 0 :
                    max_prof += prices[p] - paid
                paid = prices[p]
        return max_prof