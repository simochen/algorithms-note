# Time:  O(n)
# Space: O(1)
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        max_sum = cur_sum = nums[0]
        for n in nums[1:]:
            cur_sum = max(cur_sum + n, n)
            max_sum = max(max_sum, cur_sum)
        return max_sum