# Time:  O(1)
# Space: O(1)
class Solution:
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        str_bits = '{:b}'.format(N)
        max_len = 0
        last = str_bits.index('1')
        for i in range(last+1, len(str_bits)):
            if str_bits[i] == '1':
                if i - last > max_len:
                    max_len = i - last
                last = i
        return max_len