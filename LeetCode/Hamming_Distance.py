from collections import Counter
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        z = x ^ y
        c = Counter(bin(z))
        if '1' in c:
            return c['1']
        else:
            return 0


s = Solution()
print s.hammingDistance(2,4)
