class Solution(object):
    h_t = {}
    h_t[1] = 1
    h_t[0] = 1
       
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        Space Complexity is O(n) for hash table
        Time complexity is O(n^2)
        """
        hash_t = {}
        hash_t[0] = 1
        hash_t[1] = 1
        for i in range (2, n+1):
            bst_count = 0 
            for j in range ( 1, i+1):
                bst_count += hash_t[j-1] * hash_t[i-j]
            hash_t[i] = bst_count
        return hash_t[n]
      