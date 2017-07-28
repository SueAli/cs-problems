# Next permutation

class Solution(object):
    # Time complexity is O(n) for reverse operation

    def swap (self,nums,i,j):
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp

    def reverse (self,nums,i,j):
        while i<len(nums) and j < len(nums) and i < j :
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp
            i += 1
            j -= 1

    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        The idea is to start from the end and finding the ascending sorted
        partition start & end
        Then Find the next permutation :
        1 -->  if nums[asc_start-1] not in range ( asc_st , asc_end):
             the start of next permutaion is different from the i/p permutation
             to find the next start:
              - sort nums[asc_st : asc_end+1] into descending where nums[asc_st] < nums[asc_end]
              - swap( nums[asc-1] , nums[asc]) --> here is the solution
        2 --> else if nums[asc_st] >= nums[asc-1] >= nums[asc_end]"
            - find the smallest number(nums[j]) in nums[asc_st,asc_end+1] that is greater than nums[asc-1]
            - swap (nums[i] , nums[j])
            - sort( nums[asc_st:asc_end +1 ] into ascending order --> here is the solution



        """
        n = len(nums)
        asc_st , asc_end = n - 1, n - 1
        i = asc_st - 1

        while i >= 0 and  nums [asc_st] <= nums[ i]:
            asc_st = i
            i -= 1

        if i >= 0  :
            if not (nums[asc_st] >= nums[i]  >= nums[asc_end]) :
                self.reverse(nums,asc_st,asc_end)
                self.swap(nums,i,asc_st)

            else:
                j = asc_st
                for j in range(asc_st,asc_end+1):
                    if nums[j] > nums[i]:
                        j += 1
                    else:
                        j -= 1
                        break
                self.swap(nums,i,j)
                self.reverse(nums,asc_st,asc_end)
        else:
             self.reverse(nums,asc_st,asc_end)



