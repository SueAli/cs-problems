#https://www.interviewbit.com/problems/palindrome-partitioning/

class Solution:
    def isPalindrome(self,str, low,high):
        while low < high:
            if str[low] != str[high]:
                return False
            low += 1
            high -= 1
        return True

    def findPalindPart(self,str,start,curr_parts, result, n ): # n length of string
        if start == n:
            result.append(curr_parts[:])
            return
        for i in range(start,n):
            if self.isPalindrome(str,start,i):
                curr_parts.append(str[start:i+1])
                self.findPalindPart(str,i+1,curr_parts,result,n)
                curr_parts.pop()

    # @param A : string
    # @return a list of list of strings
    def partition(self, A):
        n = len(A)
        r = []
        self.findPalindPart(A,0,[],r,n)
        return r