# Time:  O(n)
# Space: O(1)
class Solution:
	def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        prev, current = 0, 1
        for i in range(n):
            prev, current = current, prev+current
        return current

    # Time:  O(2^n)
	# Space: O(n)
    def climbStairs1(self, n):
        if n <= 2:
            return n
        else:
            return self.climbStairs1(n-1) + self.climbStairs1(n-2)