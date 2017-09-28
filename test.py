class Trie: 
    def __init__(self):
        self.cache={}
        self.trie = {}
        self.all_possible_stmt = []
        self.curr_stmt = []
        self.dp = None
    
    def buildDp (self, s):
        n = len(s)
        self.dp = [False for i in range(n)] # n-1 locations for space
        self.dp[0] = True
        for i in range(1, n):
            for j in range(0,i): 
                if self.dp[j] and self.wordExist(s[j:i] ) :
                    self.dp[i] = True
                    break
                    
        
    def wordExist(self, word): # time comp is O(max word len)
        ptr = self.trie
        i = 0 
        while i < len(word) and word[i] in ptr: 
            ptr = ptr[word[i]]
            i += 1
            
        if i == len(word) and '#' in ptr:
            return True
        
        return False
    
        
    def buildTrie(self,wordDict):
        for word in wordDict:
            if len(word.strip()) == 0 : 
                continue
            ptr = self.trie 
            idx = 0 
            while idx < len(word):
                char = word[idx]
                if char not in ptr : 
                    ptr[char] = {}
                ptr = ptr[char]
                idx += 1
            ptr['#'] = {} # mark the word end 
            
        
    def getAllPossibleStmt(self,s, idx, root) :  
        
        
         
            
            
        
                
            
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        trie_obj = Trie()
        trie_obj.buildTrie(wordDict)
        trie_obj.buildDp(s)
        print trie_obj.dp
        trie_obj.getAllPossibleStmt(s,0,trie_obj.trie)
        return trie_obj.all_possible_stmt
        
        