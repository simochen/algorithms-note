# Time:  O(n)
# Space: O(1)
class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        prev1, cur1, prev2, cur2 = 0, nums[0], 0, nums[1]
        for i in range(1, len(nums)-1):
                prev1, cur1 = cur1, max(cur1, prev1+nums[i])
                prev2, cur2 = cur2, max(cur2, prev2+nums[i+1])
        return max(cur1, cur2)