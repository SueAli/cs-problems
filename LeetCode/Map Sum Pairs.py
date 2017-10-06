class MapSum(object):
    # time complexity is O(w)
    # Space complexity is O(w)  for recursion stack
    # where w is the average word length

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}


    def addVal(self, key, idx, val, ptr ):
        to_add = 0
        if idx == len(key): # the end of the word
            to_add = val
            if '#' in ptr: # the node alredy exist before
                to_add += (-1 * ptr['*'])
            else: # it is a new word
                ptr['#'] = {}
            return to_add

        if key[idx] not in ptr:
            ptr[key[idx]] = {'*':0}

        to_add += self.addVal(key, idx+1, val, ptr[key[idx]])
        ptr[key[idx]]['*'] += to_add
        return to_add



    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        self.addVal(key,0,val,self.trie)


    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        ptr = self.trie
        idx = 0
        while idx < len(prefix) and prefix[idx] in ptr:
            ptr = ptr[prefix[idx]]
            idx += 1
        if idx < len(prefix):
            return 0
        return ptr['*']




# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)