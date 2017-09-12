# Reverse Nodes in k-Group

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Time Complexity is O(n)
# Space Complexity is O(1)
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return head
        l_cnt = 0
        ptr = head
        while ptr:
            l_cnt += 1
            ptr = ptr.next

        if l_cnt < k:
            return head

        rounds = l_cnt / k
        act_rounds = 0
        rem = head
        final_res_start, final_res_end = None, None

        while act_rounds < rounds and rem :
            # start new round
            act_rounds += 1
            start,end = None, None
            cnt = 0
            while rem and cnt < k:
                rem_next = rem.next
                cnt += 1
                if not start :
                    start = rem

                rem.next= end
                end = rem
                rem = rem_next
            if not final_res_start :
                final_res_start = end
                final_res_end = start
            else:
                final_res_end.next = end
                final_res_end = start

        final_res_end.next = rem
        return final_res_start
