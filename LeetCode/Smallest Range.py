# Smallest Range
# Time Complexity is O( l *  k log K ) where l is the average length of lists
from heapq import heappop , heappush , heapify
import sys
class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        if len(nums) == 0 :
            return []

        min_diff = -sys.maxint
        end_ = - sys.maxint
        start_= sys.maxint

        heap_ = []
        for i in range( len(nums)):
            if len(nums[i]) > 0 :
                heap_.append((nums[i][0], i, 0 )) # val , list_idx , item_idx within this list
                end_ = max(end_,nums[i][0] )
                start_ = min(start_, nums[i][0])

        heapify(heap_) # O(k)
        min_diff = end_ - start_

        curr_end = end_
        curr_start = start_

        while heap_ :
            # check the smallest element in the heap_
            #print range_start, range_end, range_diff

            min_val , list_idx , item_idx = heap_[0]
            if curr_end - curr_start < min_diff :
                min_diff  = curr_end - curr_start
                end_ = curr_end
                start_ = curr_start

            if item_idx + 1 == len(nums[list_idx]) : # if I fininshed one list
                #the heap contains the required range
                break

            heappop(heap_)
            heappush(heap_,(nums[list_idx][item_idx+1],list_idx,item_idx+1))
            curr_end = max(curr_end , nums[list_idx][item_idx+1])
            curr_start = heap_[0][0]


        return [start_, end_]




