# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        #Time Complexity ~ O(n)
        #Space Complexity ~ O(1)
        """
        if head == None or head.next ==None:
            return head

        curr = head.next
        head.next = None
        prev = head

        while curr.next != None:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        curr.next = prev

        return curr