class Solution(object):
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        # Time complexity is O(n)
        # Space complexity is O(1)

        res = [1]
        sign = 1
        for i in range (k,0,-1):
            tmp = res[-1] + (sign*i)
            res.append(tmp)
            sign *= -1
        s = res[1] +1
        while s <= n :
            res.append(s)
            s += 1
        return res


