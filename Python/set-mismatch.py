# Time:  O(n)
# Space: O(1)
class Solution:
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s = sum(set(nums))
        repeat = sum(nums) - s
        n = len(nums)
        missing = n*(n+1)//2 - s
        return [repeat, missing]