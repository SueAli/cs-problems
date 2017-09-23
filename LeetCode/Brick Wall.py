from collections import defaultdict
# Time Complexity is O( total # bricks )
# Space Comp is O(rows) for the hashtable

class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        h_t = defaultdict(int)
        max_passed_gaps = 0

        for row in wall:
            ptr = 0
            for i in range( 0 , len(row) - 1):
                # exclude the last brick as there is no gap the vertical line can cut
                brick = row[i]
                ptr += brick
                h_t[ptr] += 1
                max_passed_gaps = max(h_t[ptr], max_passed_gaps)
                print max_passed_gaps
        return len(wall) - max_passed_gaps


