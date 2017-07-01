
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        Let's say len(nums1) = n & len(nums2)=m
        Total time complexity = O(n+m)
        Auxilary space compexity = O(n)
        """
        nums1_set= set()
        result_set = set()
        i = 0
        j = 0
        while i < len(nums1):#will be exectued n times
            nums1_set.add(nums1[i])
            i += 1

        while j < len(nums2): # will be exectued m times
            if nums2[j] in nums1_set: # looking for key in a set is O(1)
                result_set.add(nums2[j]) # O(1)
            j += 1

        return list(result_set)