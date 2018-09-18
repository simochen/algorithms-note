# Time:  O(1)
# Space: O(1)
# L, R will be integers L <= R in the range [1, 10^6]
# 10^3 ~= 2^10, 10^6 ~= 2^20
# prime: [2, 3, 5, 7, 11, 13, 17, 19]
class Solution:
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        prime = [2, 3, 5, 7, 11, 13, 17, 19]
        count = 0
        for i in range(L, R+1):
            str_bits = '{:b}'.format(i)
            if str_bits.count('1') in prime:
                count += 1
        return count