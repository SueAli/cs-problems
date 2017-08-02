# Remove Nth Node From End of List
# Time complexity is O(n)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head and n > 0:
            back,forward = head, head
            prev_back = None
            new_head = None

            while forward.next and n > 1:
                forward = forward.next
                n -= 1

            if n > 1: # len of list < n
                return head

            while forward.next :  # forward ptr reached the end
                if not new_head:
                    new_head = back
                prev_back = back
                back = back.next
                forward = forward.next

            # back ptr to element to be removed
            if not prev_back:
                new_head = back.next
            else:
                prev_back.next = back.next


            return new_head


        return head





