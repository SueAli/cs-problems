# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b
from collections import defaultdict
# Time complexity is O(n ^ 2)
# Space complexity is O(n ) for hashTable

class Solution(object):
    def gcd(self,a,b):

        while b :
            a , b = b ,a%b
        return a

    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        if len(points) <= 2:
            return len(points)
        max_points = 2
        slope_ht = defaultdict(int)
        for i in range(0 , len(points)):
            max_colinear_pts = 0
            same_pt = 1 # represent i point
            same_x = 0  # to count colinear points have x equal to the ith's x point
            same_y = 0  # to count colinear points have y equal to the ith's y  point
            slope_ht.clear()
            p1 = points[i]
            for j in range(0, len(points)):

                if i != j :
                    p2 = points[j]
                    # 1- check same point
                    if p1.x == p2.x and p1.y == p2.y:
                        same_pt +=1

                    elif p1.x == p2.x:
                        same_x += 1
                        max_colinear_pts = max( max_colinear_pts, same_x)

                    elif p1.y == p2.y:
                        same_y += 1
                        max_colinear_pts = max(max_colinear_pts, same_y)

                    else:
                        y_diff = (p1.y-p2.y)
                        x_diff = (p1.x-p2.x)
                        gcd = self.gcd(y_diff, x_diff)

                        m = (y_diff/gcd, x_diff/gcd)
                        slope_ht[m] += 1
                        max_colinear_pts = max(max_colinear_pts, slope_ht[m])

            max_points = max( max_points, max_colinear_pts+same_pt )


        return max_points



