# Time:  O(n)
# Space: O(1)
class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        prev, curr = 0, 1
        last = ""
        for c in s:
            k = 0 if c == "0" else 1
            if int(last+c) <= 26:
                prev, curr = curr*k, curr*k + prev
            else:
                if k == 0:
                    return 0
                prev = curr
            last = c
        return curr