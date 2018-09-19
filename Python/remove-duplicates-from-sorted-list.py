# Time:  O(n)
# Space: O(1)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        last = head
        curr = last.next
        while curr:
            if curr.val == last.val:
                last.next = curr.next
            else:
                last = curr
            curr = curr.next
        return head