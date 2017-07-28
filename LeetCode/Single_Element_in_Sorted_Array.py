# Single Element in a Sorted Array

class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        # Time complexity is O(log n )
        # Space Complexity is O(1)
        """
        st = 0
        end = len(nums) - 1
        mid = 0
        while st < end:
            mid = st+((end -st ) / 2)
            if mid > st and  nums[mid] == nums[mid-1] :
                if (mid -st + 1 ) % 2 == 0:
                    st = mid + 1

                else:
                    end = mid - 2


            elif mid < end  and nums[mid] == nums[mid+1]  :
                if (end - mid + 1) % 2 == 0 :
                    end = mid -1
                else:
                    st = mid + 2

            else:
                nums[mid]

        return nums[st]

