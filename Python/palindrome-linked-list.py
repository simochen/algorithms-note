# Time:  O(n)
# Space: O(1)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True
        slow, fast, _next = head, head.next, head.next
        while fast and fast.next:
            fast = fast.next.next
            rev = _next
            _next = _next.next
            rev.next = slow
            slow = rev
        if not fast:
            slow = slow.next
        while _next:
            if _next.val != slow.val:
                return False
            slow, _next = slow.next, _next.next
        return True