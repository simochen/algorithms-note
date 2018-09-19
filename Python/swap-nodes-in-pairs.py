# Time:  O(n)
# Space: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        flag = False
        curr = head
        while curr:
            if not flag:
                prev = curr
            else:
                prev.val, curr.val = curr.val, prev.val
            flag = not flag
            curr = curr.next
        return head