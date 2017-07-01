# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ### Time Complexity is O(n)
        ### Space Complexity is O(1)
        if head:
            prev = head
            curr = head.next
            while  curr:
                if prev.val == curr.val:
                    prev.next = curr.next
                else:
                    prev = curr
                curr = curr.next
        return head
