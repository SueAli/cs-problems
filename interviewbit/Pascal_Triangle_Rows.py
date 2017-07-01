class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generate(self, A):
        if A== 0:
            return []

        final_l = [[1] for x in range(0, A)]
        for i in range( 1, A):
            for j in range (1, i+1):
                if i == j:
                    final_l[i].append(1)
                else:
                    s = final_l[i-1][j] + final_l[i-1][j-1]
                    final_l[i].append(s)

        return final_l


s = Solution()
print s.generate(5)