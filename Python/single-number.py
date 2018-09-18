# Time:  O(n)
# Space: O(1)
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = 0
        for n in nums:
            c ^= n
        return c