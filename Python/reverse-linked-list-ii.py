# Time:  O(n)
# Space: O(1)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        new_head = ListNode(0)
        new_head.next = head
        curr = new_head
        for i in range(m-1):
            curr = curr.next
        left = curr
        right = curr.next
        curr = curr.next
        _next = curr.next
        for i in range(n-m):
            temp = _next
            _next = _next.next
            temp.next = curr
            curr = temp
        left.next = curr
        right.next = _next
        return new_head.next