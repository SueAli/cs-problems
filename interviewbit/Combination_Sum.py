# # https://www.interviewbit.com/problems/combination-sum/
# Given a set of candidate numbers (C) and a target number (T),
# find all unique combinations in C where the candidate numbers sums to T.

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def combinationSum(self, A, B):
        A.sort()
        res = []
        self.findComRec(B,0,len(A),A,[],res)
        return res
    # c_end is the length of the set
    def findComRec(self,T, c_st,c_end, candidates, curr_com, res):
        if T==0 and curr_com:
            res.append(curr_com[:])
            return
        if  c_st == c_end:
            return
        for i in range(c_st,c_end):
            if i < (c_end-1) and candidates[i] == candidates[i+1]:
                continue
            if candidates[i] <= T:
                count = T / candidates[i]
                while count > 0 :
                    curr_com+= [candidates[i]] * count
                    self.findComRec(T-(candidates[i]*count), i+1,c_end,candidates,curr_com,res)
                    for j in range(0, count):
                        curr_com.pop()
                    count -= 1
