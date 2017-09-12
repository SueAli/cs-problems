#  Judge Route Circle
class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        # Time Comp O( len(moves))
        # Space Comp is O(1)

        x,y = 0,0
        for m in moves:
            if m == "U":
                y += 1
            elif m == "D":
                y -= 1
            elif m == "R":
                x += 1
            else:
                x -= 1
        if  x == 0 and y == 0 :
            return True
        return False
