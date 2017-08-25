# Count of Smaller Numbers After Self
# Time complexity is O(n* log n )
# space complexity is O( n ) for merge operation

class Solution(object):
    def merge(selfs, nums,idx_arr, l1, r1, l2, r2, res):
        start = l1
        sorted_idx = [0 for i in range(r2-l1+1)]
        p = 0
        came_befor_me = 0
        while l1 <= r1 or l2 <= r2:
            if l1 > r1 : # start moving all elements from right part
                sorted_idx[p] = idx_arr[l2]
                l2 += 1
            elif l2 > r2:
                sorted_idx[p] = idx_arr[l1]
                res[idx_arr[l1]] += came_befor_me
                l1 += 1
            elif nums[idx_arr[l1]] > nums[idx_arr[l2]]:
                sorted_idx[p] = idx_arr[l2]
                came_befor_me += 1
                l2 += 1
            else:
                sorted_idx[p] = idx_arr[l1]
                res[idx_arr[l1]] += came_befor_me
                l1 += 1
            p += 1
        # update index to match the sorted one
        for i in range ( 0, len(sorted_idx)):
            idx_arr[start+i] = sorted_idx[i]






    def mergeSort(self, nums, idx_arr, l,r , res):
        if l >= r:
            return
        mid = (l+r)/2
        self.mergeSort(nums, idx_arr, l, mid, res)
        self.mergeSort(nums, idx_arr, mid+1, r, res)
        self.merge(nums, idx_arr, l,mid, mid+1,r,res)

    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        n = len(nums)
        res = [0 for i in range(n)]
        idxx = [i for i in range(n)]
        self.mergeSort(nums,idxx,0,n-1,res )
        return res
