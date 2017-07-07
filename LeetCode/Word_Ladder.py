from collections import deque
import string
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        # BFS Breadth First Search , Word Ladder
        # Time complexity is O ( w * m ) where w is the len of wordList and m is the averge word len
        # Space Complexity is O ( w )
        """
        words_dic = set(wordList) # memory = len(wordList)
        if (beginWord != endWord and endWord in words_dic):
            trans_len = 0
            q = deque()
            visited = set()
            visited.add(beginWord) # memory = len(wordList) = w
            q.append(beginWord) # memory = len(wordList) = w
            while q:   # W
                curr_len = len(q)
                trans_len += 1
                for i in xrange(0, curr_len):
                    currWord = q.popleft()
                    for idx, c in enumerate(currWord): # m where m is the average word len
                        for new_c in string.lowercase: # 26
                            if c != new_c :
                                tmp_word = (currWord[0:idx] + new_c + currWord[idx+1:])
                                if tmp_word == endWord:
                                    return trans_len + 1
                                if tmp_word not in visited and tmp_word in words_dic:
                                    visited.add(tmp_word)
                                    q.append(tmp_word)
        return 0












