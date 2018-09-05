# Time:  O(n)
# Space: O(1)
class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev, current = 0, 0
        for n in nums:
            prev, current = current, max(current, n+prev)
        return current