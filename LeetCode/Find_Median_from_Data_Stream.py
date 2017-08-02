# Find Median from Data Stream

import heapq
class MaxHeapElem:
    def __init__(self,x):
        self.val = x
    def __lt__(self,other):
        return self.val >= other.val

class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.part1_max_heap = []
        self.part2_min_heap = []


    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        # TIME COMPLEXITY IS Log(n) to heapify the heap
        if len(self.part1_max_heap) == 0:
             heapq.heappush(self.part1_max_heap,MaxHeapElem(num))

        elif   num <= self.part1_max_heap[0].val:
            heapq.heappush(self.part1_max_heap,MaxHeapElem(num))

            if len(self.part1_max_heap) > len(self.part2_min_heap):
                 heapq.heappush( self.part2_min_heap ,  heapq.heappop(self.part1_max_heap).val)

        else:
            heapq.heappush(self.part2_min_heap,num)
            if len(self.part2_min_heap) >  len(self.part1_max_heap) :
                heapq.heappush( self.part1_max_heap  ,  MaxHeapElem( heapq.heappop(self.part2_min_heap)))




    def findMedian(self):
        """
        :rtype: float
        """
        # Time Complexity is O(1)

        if len(self.part1_max_heap) > len(self.part2_min_heap):
            return float(self.part1_max_heap[0].val)

        elif len(self.part1_max_heap) < len(self.part2_min_heap):
            return float(self.part2_min_heap[0])
        else:
            return float(self.part1_max_heap[0].val + self.part2_min_heap[0])/2





# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()