# Delete Operation for Two Strings
import sys
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        # Time complexity is O(len(word1) * len(word2))
        # Space compexity is O(len(word1) * len(word2))
        """

        cache = {}
        def minDisRec(word1, idx1, word2, idx2):
            if idx1 == len(word1) and idx2 == len(word2):
                return 0
            elif idx1 < len(word1) and idx2 == len(word2):
                return len(word1) - idx1
            elif idx2< len(word2) and idx1 == len(word1):
                return len(word2) - idx2
            else:
                if (idx1,idx2) not in cache:
                    if word1[idx1] == word2[idx2]:
                        cache[(idx1,idx2)] =  minDisRec(word1,idx1+1, word2,idx2+1)

                    else:
                        cache[(idx1,idx2)] =  1 + min( minDisRec(word1,idx1+1, word2, idx2),
                                       minDisRec(word1,idx1, word2,idx2+1)
                        )
                return cache[(idx1,idx2)]
        return minDisRec(word1, 0, word2, 0)
