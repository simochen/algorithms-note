# Time:  O(logN)
# Space: O(1)
class Solution:
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        d_self = [0]
        d_diff = [0]
        for i in range(10):
            d_self.append(d_self[-1])
            d_diff.append(d_diff[-1])
            if i in [0, 1, 8]:
                d_self[-1] += 1
            elif i in [2, 5, 6, 9]:
                d_diff[-1] += 1
            
        cur_diff, cur_all = 0, 1
        b = 0
        while N > 0:
            prev_diff, prev_all = cur_diff, cur_all
            r = N % 10
            total = pow(7,b)
            cur_all = (d_diff[r] + d_self[r]) * total
            cur_diff = cur_all - d_self[r] * pow(3,b)
            if r in [0, 1, 8]:
                cur_diff += prev_diff
                cur_all += prev_all
            elif r in [2, 5, 6, 9]:
                cur_diff += prev_all
                cur_all += prev_all
            N //= 10
            b += 1
        return cur_diff