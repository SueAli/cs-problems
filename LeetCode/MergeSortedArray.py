# Merge Sorted Array
# Time Complexity O(m+n)

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        curr = n + m - 1 
        ptr1 = m - 1 
        ptr2 = n - 1 

        while(curr >= 0) :

            if(ptr1 < 0 or ptr2 < 0) :
                break
            if nums1[ptr1] > nums2[ptr2]:
                nums1[curr] = nums1[ptr1]
                ptr1 -= 1

            elif nums1[ptr1] < nums2[ptr2]:
                nums1[curr] = nums2[ptr2]
                ptr2 -= 1

            else:
                nums1[curr] = nums1[ptr1]
                curr -= 1
                nums1[curr] = nums2[ptr2]
                ptr1 -= 1
                ptr2 -= 1
            curr -= 1


        while ( ptr1 >= 0):
            nums1[curr] = nums1[ptr1]
            ptr1 -= 1
            curr -= 1
        while (ptr2 >= 0) :
            nums1[curr] = nums2[ptr2]
            ptr2 -= 1
            curr -= 1
        
