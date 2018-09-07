# Time:  O(m*n)
# Space: O(m)
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid[0])
        arr = [0 for i in range(m+1)]
        for i in range(len(obstacleGrid)):
            for j in range(m):
                if obstacleGrid[i][j]:
                    arr[j+1] = 0
                else:
                    if i == 0 and j == 0:
                        arr[1] = 1
                    else:
                        arr[j+1] += arr[j]
        return arr[-1]