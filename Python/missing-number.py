# coding=utf-8
# Time:  O(n)
# Space: O(1)

class Solution(object):
	# 解法1：与1-(n-1)异或(与0异或等于本身)，若某数存在则被抵消
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lost = 0
        for i in range(len(nums)):
            lost ^= nums[i] ^ (i+1)
        return lost
    
	# 解法2：0-(n-1)的和减去数组中所有数的和
	def missingNumber1(self, nums):
	    k = len(nums)
	    s = k * (k+1) / 2
	    for i in range(k):
	       s -= nums[i]
	    return s