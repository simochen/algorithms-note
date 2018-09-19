# Time:  O(n)
# Space: O(1)

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
        """
        if not head:
            return head
        prev = head
        curr = head.next
        while curr:
            _next = curr.next
            curr.next = prev
            prev = curr
            curr = _next
        head.next = None
        return prev