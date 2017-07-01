class Solution(object):
    def getSum(self, a, b):
    # python represents negative numbers using infinite 2's complement
    # ex: -4 --> .....111111011
    # Addition equal to the results of a XOR b and carry = a & b
    # In case of having negative numbers the carry will never set to zero as a result of
    # anding it with the infinite 2's complement of one of the input
    # Sp to solve it once the carry bit shifted beyond highest bit in the input
    # the algorithm should return the results
        MAX_BIT = 2**32
        MAX_BIT_COMPLIMENT = -2**32
        while b != 0:
            if b == MAX_BIT:
                return a ^ MAX_BIT_COMPLIMENT
            carry = a & b
            a = a ^ b
            b = carry << 1
        return a

    # Recursive implementation
    def getSumRecursive(self, a, b):
        MAX_BIT = 2**32
        MAX_BIT_COMPLIMENT = -2**32
        while b != 0:
            if b == MAX_BIT:
                return a ^ MAX_BIT_COMPLIMENT
            carry = a & b
            a = a ^ b
            b = carry << 1
            self.getSumRecursive(a,b)
        return a



# Testing
s = Solution()
print "Sum(-3,3)= ",s.getSum(-3,3)
print "Sum(7,3)= ",s.getSumRecursive(1000,-500)




