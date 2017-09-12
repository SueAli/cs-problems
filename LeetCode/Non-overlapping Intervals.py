# Non-overlapping Intervals
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    # Time complexity is O( n log n )


    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        cnt = 0
        if len(intervals) > 0 :
            intervals.sort(key=lambda x: x.start) # n log n # sort on start first then on the end
            curr_end = intervals[0].end
            for i in range (1,len(intervals)):
                if intervals[i].start < curr_end:
                    cnt += 1
                    curr_end = min(intervals[i].end, curr_end)
                else:
                    curr_end = intervals[i].end

        return cnt