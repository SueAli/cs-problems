import  copy
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def combinationSum(self, A, B):
        # B is target
        finalList=[]
        A.sort()
        def findCombSum(start, currentSum, currCombList,inputList):

            if currentSum > B:
                return
            if currentSum == B:
                finalList.append(copy.copy(currCombList))
                print currCombList

            prev = -1
            for i in range(start,len(inputList) ):
                if inputList[i] != prev: # To skip simialr items iteration
                    currCombList.append(inputList[i])
                    currentSum += inputList[i]
                    findCombSum(i+1,currentSum,currCombList,inputList)
                    if len(currCombList) >0:
                        currentSum -= inputList[i]
                        currCombList.pop()
                prev = inputList[i]

        findCombSum(0,0,[],A)
        return finalList


s = Solution()
s.combinationSum([10,1,2,7,6,1,5],8)