# Time:  O(1)
# Space: O(1)
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        # str_bits = bin(n)
        str_bits = '{:b}'.format(n)
        return str_bits.count('1') == 1