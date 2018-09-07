# Time:  O(m*n)
# Space: O(m)
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid[0])
        arr = [0 for i in range(m)]
        for i in range(len(grid)):
            for j in range(m):
                if j == 0:
                    arr[j] += grid[i][j]
                elif i == 0:
                    arr[j] = arr[j-1] + grid[i][j]
                else:
                    arr[j] = min(arr[j-1],arr[j]) + grid[i][j]
        return arr[-1]