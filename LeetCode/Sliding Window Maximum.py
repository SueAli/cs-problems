from  heapq import heappop , heappush, heapify

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Time comlpexity is O(n * k log k )
        # Space Complesixty is O(k)

        res = []
        if len(nums) > 0 :
            heap_ = []
            i = 0
            while i < k and i < len(nums): # add the first k values to the heap
                heap_.append((-1 * nums[i], i))
                i += 1
            heapify(heap_) # almost O(k)
            res.append(-1 * heap_[0][0])

            while i < len(nums): # n
                heappush(heap_, (-1 * nums[i],i)) # k log k
                while heap_[0][1] <= (i-k )   :
                    heappop(heap_) # k log k
                res.append(-1 *heap_[0][0])
                i+= 1
        return res





            