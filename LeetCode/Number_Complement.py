class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        #O(n) time where n is the number of bits in the input num
        #O(1) space memory
        ## Another Solution to num ^ int("".join([1 for i in range(0, len(bin(num)) -2 )]))

        n_bin = bin(num).split("b")[1].replace('1','$').replace('0','1').replace('$','0')
        return int(n_bin,2)
