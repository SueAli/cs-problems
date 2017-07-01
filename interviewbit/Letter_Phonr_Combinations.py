class Solution:
    # @param A : string
    # @return a list of strings
    ### Time Complexity is O(3 ^ n ) , where n is the length of the input string
    ### Space Complexity is O(n) for recursive function stack
    def __init__(self):
        self.mapping = { '0':'0','1':'1','2':'abc','3':'def','4':'ghi', '5':'jkl', '6':'mno',
                        '7':'pqrs','8':'tuv','9':'wxyz'}
        self.result = []

    def getCombinationsRec(self, A, r, start, end, curr_comb ):
        if start > end:
            r.append("".join(curr_comb))
            return
        curr_digit = A[start]
        digit_mapping = self.mapping[curr_digit]
        for c in digit_mapping:
            curr_comb.append(c)
            self.getCombinationsRec(A,r,start+1,end,curr_comb)
            curr_comb.pop()

    def letterCombinations(self, A):
        self.getCombinationsRec(A, self.result,0, len(A) -1, [])
        return self.result



