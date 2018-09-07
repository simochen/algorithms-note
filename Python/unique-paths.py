# Time:  O(m*n)
# Space: O(m)
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        arr = [0 for i in range(m+1)]
        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    arr[1] = 1
                else:
                    arr[j+1] += arr[j]
        return arr[-1]