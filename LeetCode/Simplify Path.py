# Simplify Path

class Solution(object):
   ''


   def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """

        i = 0
        s = []

        while  i < len(path):
            j = i +1

            while j < len(path) and path[j] != '/':
                j += 1

            if j- i-1 > 0:  # the len of dir
                start = i+1
                i = j
                if path[start:j] == '..' :
                    if s:
                        s.pop()
                elif  path[start:j] =='.':
                    continue
                else:
                    s.append('/'+ path[start:j] )
            i = j

        if not s:
            return '/'
        else:
            return ''.join(s)








