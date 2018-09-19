# Time:  O(m+n)
# Space: O(1)
# the length of the intersection is the same

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        pointerA, pointerB = headA, headB
        while pointerA is not pointerB:
            pointerA = headB if not pointerA else pointerA.next
            pointerB = headA if not pointerB else pointerB.next
        return pointerA