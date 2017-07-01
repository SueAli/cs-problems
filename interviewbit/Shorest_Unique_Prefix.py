class TrieNode:
    def __init__(self):
        self.children = dict()
        self.freq= 1
        self.leaf = False

class Solution:
    def  buildTrie(self, strList):
        root = TrieNode()
        curr = root
        for item in strList:
            for c in item:
                if c in curr.children:
                    curr.children[c].freq += 1
                else:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]

            curr.leaf = True
            curr = root
        return root
    def findUniquePrefix(self, word, root):
        pre =""
        i = 0
        curr = root
        while i < len(word) and word[i] in curr.children :
            pre  += word[i]
            if curr.children[word[i]].freq == 1:
                return pre
            else:
                curr = curr.children[word[i]]
                i +=1
        return pre

    def prefix(self, A):
        root = self.buildTrie(A)
        result = []
        for word in A:
            result.append(self.findUniquePrefix(word,root))
        return result