# Group Anagrams
# Given an array of strings, group anagrams together.



class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        Time complexity is O(n * m log m )
        """
        res =[]
        h = {}
        for s in strs: # O(n )
            t = "".join(sorted([c for c in s])) #m log m where m the average len of str
            if t not in h:
                h[t] = []
                res.append(h[t])
            h[t].append(s)
        return res

