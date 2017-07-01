import math
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Time Complexity = O(n) --> Time to loop on all hash_t elements
        Space Complexity = O(n) --> the worst case all input array elements will be unique
        """
        hash_t = {}
        majorityElemCount = math.floor(len(nums)/2.0)
        i = 0
        curr_ocr = 0
        while i < len(nums):

            if nums[i] in hash_t: #O(1)
                hash_t[nums[i]] += 1 #O(1)
                curr_ocr = hash_t[nums[i]]
            else:
                hash_t[nums[i]] = 1
                curr_ocr = 1

            if curr_ocr > majorityElemCount:
                return nums[i]
            i += 1

        return None


