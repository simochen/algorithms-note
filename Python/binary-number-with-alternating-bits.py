# Time:  O(logn)
# Space: O(1)
class Solution:
    def hasAlternatingBits(self, n):
        num = n ^ (n >> 1)
        return not (num & (num + 1))

    def hasAlternatingBits1(self, n):
        """
        :type n: int
        :rtype: bool
        """
        last = n & 1
        n = n >> 1
        while n > 0:
            curr = n & 1
            if not curr ^ last:
                return False
            last = curr
            n = n >> 1
        return True