class Solution(object):
    def bits2time(self, bits):
        hour = int(bits[:4], 2)
        minite = int(bits[4:], 2)
        if hour > 11 or minite > 59:
            return None
        else:
            return '{:d}:{:02d}'.format(hour, minite)
        
    def num2bits(self, n, N, list_bits):
        if n == N:
            return [s+"1"*N for s in list_bits]
        elif n == 0:
            return [s+"0"*N for s in list_bits]
        else:
            return self.num2bits(n, N-1, [s+"0" for s in list_bits]) + self.num2bits(n-1, N-1, [s+"1" for s in list_bits])

    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        list_bits = self.num2bits(num, 12, [""])
        times = []
        for s in list_bits:
            time = self.bits2time(s)
            if time != None:
                times.append(time)
        return times

    def readBinaryWatch1(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        res = []
        for h in range(12):
            for m in range(60):
                if (bin(h)+bin(m)).count('1') == num:
                    res.append('{:d}:{:02d}'.format(h, m))
        return res