import string
class MagicDictionary(object):
    # Space comp is O(d * w) where d is the dic len and w is the avg word len
    # Time Comp is O(26 * w ) = O(w )
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashtable = set()


    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        for s in dict :
            self.hashtable.add(s)


    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """


        for c in string.ascii_lowercase: # Time Comp is O ( 26 * w )
            for i in range(0, len(word)):
                if c != word[i]:
                    tmp = word[0:i]+ c + word[i+1:]
                    if tmp in self.hashtable:
                        return True
        return False






# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)