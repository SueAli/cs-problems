class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        def searchPrefixTree(root, word, idx, pref_tree):
            if idx == len(word) and '#' in root:
                return True
            if idx < len(word) :
                return ( word[idx] in root and
                        searchPrefixTree(root[word[idx]], word, idx+1, pref_tree)
                       ) or  ('#' in root and searchPrefixTree(pref_tree, word, idx, pref_tree))
            return False


        def addWord (root, word):
            ptr = root
            idx = 0
            while idx < len(word):
                c = word[idx]
                if c not in ptr :
                    ptr[c] = {}
                ptr = ptr[c]
                idx += 1
            ptr['#']={}

        words.sort(key = len)
        res = []
        pref_tree = {}

        for word in words:
                if len(word) == 0 :
                    continue
                if searchPrefixTree(pref_tree, word, 0,pref_tree):
                    # time avg_word_len * array size
                    # space complexity is  avg_word_len * array size  for recursion stack
                        res.append(word)
                else:
                    addWord(pref_tree, word)

        return res





