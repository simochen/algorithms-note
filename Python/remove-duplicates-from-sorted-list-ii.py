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
        new_head = ListNode(0)
        new_head.next = head
        prev = new_head
        flag = True
        while prev.next:
            curr = prev.next
            while curr.next and curr.next.val == curr.val:
                flag = False
                curr.next = curr.next.next
            if not flag:
                prev.next = curr.next
                flag = True
            else:
                prev = curr
        return new_head.next