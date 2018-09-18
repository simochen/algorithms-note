# Time:  O(1)
# Space: O(1)
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        str_bits = '{:032b}'.format(n)
        return str_bits.count('1')

    def hammingWeight1(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        for i in range(32):
            bit = n & 1
            if bit == 1:
                count += 1
            n = n >> 1
        return count