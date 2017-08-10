class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}



    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        ptr = self.root
        for i in range(len(word)):
            w = word[i]
            if w not in ptr :
                ptr[w] = {}
            ptr = ptr[w]
            if i == len(word) -1 :
                ptr['#'] =None # mark word ending






    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        ptr = self.root
        i = 0
        while i < len(word) and word[i] in ptr:
            ptr = ptr [word[i]]
            i += 1
        if i == len(word) and '#' in ptr:
            return True
        return False


    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        ptr = self.root
        i = 0
        while i < len(prefix) and prefix[i] in ptr:
            ptr = ptr [prefix[i]]
            i += 1
        if i == len(prefix) :
            return True
        return False



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)