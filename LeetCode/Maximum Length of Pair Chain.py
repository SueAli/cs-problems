#Maximum Length of Pair Chain

class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        # Dynamic programing bottom-up (tabular form) extra memory but not very useful here
        # DP code is commented
        # so it can be solved iterative
        # Time Complexity is O(n) + O(n log n ) = O( n log n )
        # Space complexity is O( 1 )
        n = len(pairs)
        pairs.sort(key = lambda x:(x[0],x[1])) # n* log n
        # chain = [ [1,1] for i in range(n)] #(chain_len, chain_end)
        # chain [0] = [1,pairs[0][1]]
        chain_len, chain_end = 1, pairs[0][1]
        for p in range(1,n) :
            if pairs[p][0] <= chain_end:
                #chain[p][0] = chain[p-1][0] # same chain len that end at this point
                #chain[p][1] = min(chain[p-1][1], pairs[p][1]) # choose the min end
                chain_end = min(chain_end, pairs[p][1])
            else:
                #chain[p][0] = chain[p-1][0] +1
                chain_len += 1
                #chain[p][1] = pairs[p][1]
                chain_end = pairs[p][1]

        return chain_len


