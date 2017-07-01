class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool

        """

        # ------------ usnig Sorting ----------------
        def containsDuplicateSortingMethod(nums_input):
            #Time = O(n) + O(nlogn ) ~ O( n log n )
            #Extra Memory ~ O(1)
            nums_input.sort() # O(nlogn)
            for i in range(0, len(nums_input) -1): # O(n)
                if nums_input[i] == nums_input[i+1]:
                    return True
            return False

        #----------- using hashtable -------------------
        def containsDuplicateHashTable(nums_input):
            #Time Complexity ~ O(n)
            #Space Complexity ~ O(n)
            s =set()
            for i in range (0, len(nums_input)):
                if nums_input[i] in s:
                    return True
                else:
                    s.add(nums_input[i])
            return False
        #------------------------------------------------
        return containsDuplicateHashTable(nums)
