
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        Let's say len(nums1) = n & len(nums2)=m
        Total time complexity = O(min(n,m)) + O(n * logn) + O(m * log m)
        Auxilary space compexity = O(1)
        """
        inter= set()
        i = 0 
        j = 0 
        nums1.sort() 
        nums2.sort()
        
        while j < len(nums2) and i < len(nums1):
            if nums1[i] == nums2[j]:
                inter.add(nums2[j])
                j += 1
                i += 1
            elif  nums1[i] <  nums2[j]:
                 i += 1
            else:
                 j += 1
        return list(inter)