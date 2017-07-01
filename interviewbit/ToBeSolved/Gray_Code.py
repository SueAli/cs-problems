class Solution:
    # https://www.interviewbit.com/problems/gray-code/
    # @param A : integer
    # @return a list of integers
    def grayCode(self, A):
        # Recursion Solution
        # Time Complexity = n * 2^n
        # Space Complexity = n * 2^n. n for stack functions call and each call new list will be created with
        # length 2^n
        def getGrays(n):
            print "Call for n =", n
            if n == 0 :
                return [0]
            grays = getGrays(n-1)
            print grays
            for i in range(len(grays)-1,-1,-1):
                grays.append(grays[i] ^ (1 << (n-1)))
            return grays
        return getGrays(A)
        # Iterative Solution is more optimal
        # Time complexity is 2 ^n
        # Space complexity is O(1)
        #ans=[]
        #Iterative Solution : O(n)
        # Space complexity O(1) regardless space for the result returned
        # for i in range(2**A):
        #     ans.append((i>>1)^i)
        # return ans
        # print ansr


S = Solution()
print S.grayCode(3)