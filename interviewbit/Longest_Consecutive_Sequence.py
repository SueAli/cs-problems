class Solution:
    # @param A : tuple of integers
    # @return an integer
    # Time complexity is O(n)
    # Space Complexity is O(n) for the hash table
    def longestConsecutive(self, A):
        if not A or len(A) == 0:
            return 0
        hash_t ={}
        longest_path = 1
        for item in A:
            if not item in hash_t :
                hash_t[item] = 1

        for item in A:
            if item in hash_t:
                curr = item
                while curr+1 in hash_t:
                        hash_t[item] = hash_t[curr+1] + hash_t[item]
                        if hash_t[item]  > longest_path:
                            longest_path = hash_t[item]
                        del hash_t[curr+1]
                        curr = curr+1
        return longest_path

