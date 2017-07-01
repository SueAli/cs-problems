import heapq
import math
class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return an integer
    # Time complexity is O(n) + k * log (n)
    # Space Complexity if we can not make any changes in the input array, extra space memory of O(n) will be
    # required to build the heap
    def nchoc(self, A, B):
        r =0
        m =  ((10**9)+7)
        h = [ item * -1 for item in B] # O(n)
        heapq.heapify(h)  # O(n)
        for i in range(0,A):
            curr = h[0] * -1
            r =  r + curr
            heapq.heapreplace(h,-1 *int(math.floor(curr/2.))) #(log n)
        return int(r) % m


s = Solution()
print s.nchoc(10, [ 2147483647, 2000000014, 2147483647 ])

#284628164


