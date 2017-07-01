class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    # Time Complexity is O(n)
    # Space Complexity is O(K) for hash table
    def dNums(self, A, B):
        if B > len(A):
            return []
        n = len(A)
        hash_t = {}
        r = []
        dist =0
        for j in range (0, B):
            if A[j] in hash_t:
                hash_t[A[j]] += 1
            else:
                hash_t[A[j]] = 1
                dist += 1

        r.append( dist)
        i = B
        while i < n:
            hash_t[A[i-B]] -= 1
            if hash_t[A[i-B]] == 0 :
                dist -= 1
                del  hash_t[A[i-B]]

            if A[i] in hash_t :
                hash_t[A[i]] += 1
            else:
                dist += 1
                hash_t[A[i]] = 1
            r.append( dist)
            i += 1
        return r


