# Merge k Sorted Lists

# What is the time complexity for this one ??


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def mergeTwoLists(self,L1, L2):
        if not L1:
            return L2
        if not L2:
            return L1
        else:
            merged_head = L1 if L1.val < L2.val else L2
            merged_end = merged_head
            L1_prv , L2_prv = None , None

            while L1 and L2:
                while L2 and L1 and L1.val >= L2.val:
                    L2_prv = L2
                    L2 = L2.next

                if L2_prv :
                    L2_prv.next = L1
                    l2_prv = None

                while L2 and L1 and L2.val >= L1.val:
                    L1_prv = L1
                    L1 = L1.next

                if L1_prv :
                    L1_prv.next = L2
                    L1_prv = None

            return merged_head


    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        res = None
        for i in range(len(lists)):
            res = self.mergeTwoLists(res, lists[i])
        return res