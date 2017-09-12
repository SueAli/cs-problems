# Reverse Linked List II
# TIME COMPLEXITY IS O(N)
# SPACE COMPLEXITY IS O(1)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if  head :
            before_start = None
            cnt = 1
            ptr = head
            while cnt < m:
                cnt += 1
                before_start = ptr
                ptr = ptr.next
            reverse_start , reverse_end = ptr, ptr
            ptr = ptr.next
            while cnt < n :
                cnt += 1
                ptr_next = ptr.next
                ptr.next = reverse_end
                reverse_end = ptr
                ptr = ptr_next
            if before_start:
                before_start.next  = reverse_end
            else:
                head = reverse_end
            reverse_start.next = ptr
        return head
