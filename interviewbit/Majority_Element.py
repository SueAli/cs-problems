# Majority Element
# https://www.interviewbit.com/problems/majority-element/#
class Solution:
    # @param A : tuple of integers
    # @return an integer
    ## Assuming there is only one majority element
    ## Time Complexity is O(n)
    ## Space Complexity is O(n)
    def majorityElement(self, A):
        hash_t = dict()
        for item in A:
            if item in hash_t:
                hash_t[item] += 1
            else:
                 hash_t[item] = 1

        for k,v in hash_t.iteritems():
            if v > math.floor(len(A)/2):
                return k
        return -1


