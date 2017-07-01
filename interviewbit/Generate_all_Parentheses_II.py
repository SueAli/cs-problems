
class Solution:
    # @param A : integer
    # @return a list of strings
    def generateParenthesis(self, A):
        p_list = []
        mid = A
        sting =""
        def getParenthesis(pToOpen,pToClose, string, p_list):
            if pToOpen == 0 and pToClose == 0 :
                p_list.append(string)
                print string
            if pToOpen > pToClose:
                return
            if pToOpen > 0:
                getParenthesis(pToOpen-1,pToClose,string+"(",p_list)
            if pToClose > 0:
                getParenthesis(pToOpen,pToClose-1,string+")",p_list)

        getParenthesis(mid,mid, sting,p_list)
        return p_list


s = Solution()
print  s.generateParenthesis(0)