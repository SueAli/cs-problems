# Time Complexity is O(n choose k)
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        def getComb (st_idx, n , k , curr_comb, final_res):
            if k == 0 :
                final_res.append(curr_comb[:])
                return
            for i in xrange(st_idx, n +1):
                curr_comb.append(i)
                getComb(i+1, n , k-1, curr_comb, final_res)
                curr_comb.pop()
        if k <= n :
            getComb (1, n , k , [], res)
        return res