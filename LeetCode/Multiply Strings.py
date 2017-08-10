"""
Multiply strings
Time complexity is n1 * n2
Space complexity is constant
"""

class Solution(object):
    def multiply(self, nums1, nums2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        n2 = len(nums2)-1
        f_res = 0
        n = len(nums2)
        while  n2 >= 0 :
            c = 0
            level = 0
            res = 0
            n1 = len(nums1)-1
            while n1 >= 0 :
                m = (int(nums1[n1]) * int(nums2[n2])) + c

                s = m % 10
                c = m / 10
                res +=  (10 ** level) * s
                level += 1
                n1 -= 1

            res += (10 ** level ) * c
            f_res += ( 10 **(n-n2-1)) * res
            n2 -= 1
        return str(f_res )



