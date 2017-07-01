import collections
class Solution(object):
    def intersectHash(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        n = len(nums1)
        m = len(nums2)
        Time Complexity ~ O(min(m, n) + max(m, n)) ~ O(m+n)  --> cost of building hash table for the list of smallest length
        Space Complexity ~ O(min(m,n)) --> for the hash table
        """
        def inter (l1, l2):
            #l1 has the samallest items
            out =[]
            hash_t = collections.Counter(l1)
            for item in l2:
                if item in hash_t:
                    if hash_t[item] > 0:
                        hash_t[item] -=1
                        out.append(item)

            return out
        if len(nums1) < len(nums2):
            return inter(nums1,nums2)
        else:
            return inter(nums2,nums1)

    def intersectSorting(self,nums1,nums2):
        '''
         Time Complexity : O(n * log n + m * log m)
         Space Complexity : min(n,m) For intersection items
        '''

        nums1.sort() # O(nlogn)
        nums2.sort() # O(mlogm)
        n1_i=0
        n2_i =0
        intersect=[]
        while n1_i < len(nums1) and n2_i < len(nums2):
            if nums1[n1_i] == nums2[n2_i]:
                intersect.append(nums1[n1_i])
                n1_i += 1
                n2_i += 1

            elif nums1[n1_i] < nums2[n2_i]:
                n1_i += 1

            else:
                n2_i += 1

        return intersect


#Testing
s = Solution()
print s.intersectHash([1,2,2,3],[2,1])