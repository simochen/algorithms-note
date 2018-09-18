# Time:  O(1)
# Space: O(1)
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        sn = '{:032b}'.format(n)
        sn = sn[::-1]
        return int(sn, 2)

    def reverseBits1(self, n):
        reverse = 0
        for i in range(32):
            reverse = reverse << 1
            bit = n & 1
            reverse += bit
            n = n >> 1
        return reverse