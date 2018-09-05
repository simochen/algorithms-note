# Time:  ctor:   O(n),
#        lookup: O(1)
# Space: O(n)
class NumArray:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        N = len(nums)
        self.arr = [0]
        for i in range(N):
            self.arr.append(self.arr[-1] + nums[i])

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.arr[j+1]-self.arr[i]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)