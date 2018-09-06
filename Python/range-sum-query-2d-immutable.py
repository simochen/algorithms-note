# Time:   O(m*n)
# lookup: O(1)
# Space:  O(m*n)
class NumMatrix:

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        M = len(matrix)
        if M == 0:
            N = 0
        else:
            N = len(matrix[0])
        self.arr = []
        for i in range(M):
            self.arr.append([0])
            for j in range(N):
                self.arr[i].append(self.arr[i][-1] + matrix[i][j])
        for j in range(1, N+1):
            for i in range(1, M):
                self.arr[i][j] += self.arr[i-1][j]
        self.arr.insert(0, [0 for j in range(N+1)])               

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.arr[row2+1][col2+1] - self.arr[row2+1][col1] - self.arr[row1][col2+1] + self.arr[row1][col1]

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)