# Edit Distance

class Solution(object):

    def getMinEdits(self,w1, w2, word1, word2,cache):
        if (w1,w2) in cache:
            return cache[(w1,w2)]
        if w2 >= len(word2) and w1 < len(word1):
             return len(word1) - w1
        if w1 >= len(word1)    and w2 < len(word2):
            return len(word2) - w2

        min_edits = 0
        while w1 < len(word1) and w2 < len(word2) and word1[w1] == word2[w2]:
            w1 += 1
            w2 += 1

        if w2 < len(word2) or w1 < len(word1):
            min_edits += 1 + min(
                self.getMinEdits(w1+1, w2+1, word1, word2,cache), # replace chr in word1
                self.getMinEdits(w1, w2+1, word1, word2,cache), # insert new chr in word1
                self.getMinEdits(w1+1,w2,word1,word2,cache)# delete chr from word1
            )
        cache[(w1,w2)] = min_edits
        return min_edits


    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        cache = {}
        return self.getMinEdits(0,0,word1,word2,cache)
