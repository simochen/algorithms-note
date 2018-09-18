# Time:  O(1)
# Space: O(1)
class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        if b == 0:
            return a
        
        bit_length = 32
        neg_bit, mask = (1 << bit_length) >> 1, ~(~0 << bit_length)
        a = (a | ~mask) if (a & neg_bit) else (a & mask)
        b = (b | ~mask) if (b & neg_bit) else (b & mask)

        s = a ^ b
        carry = (a & b) << 1
        return self.getSum(s, carry)