#  Repeated DNA Sequences

from collections import defaultdict
class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        h_t = defaultdict(int)
        i,j = 0,  9
        res = []
        while i < len(s) and j < len(s):
            h_t[s[i:j+1]] += 1
            i += 1
            j += 1
        for k,v in h_t.iteritems():
            if v >1 :
                res.append(k)
        return res





