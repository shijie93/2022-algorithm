
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        height = len(matrix)
        width = len(matrix[0])

        self.up = [[0] * (width + 1) for _ in range(height + 1)]


        for i in range(1, height + 1):
            for j in range(1, width + 1):
                self.up[i][j] = self.up[i - 1][j] + self.up[i][j - 1] - self.up[i - 1][j - 1] + matrix[i - 1][j - 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.up[row2 + 1][col2 + 1] - self.up[row1 - 1 + 1][col2 + 1] - self.up[row2 + 1][col1 - 1 + 1] + self.up[row1 + 1 - 1][col1 + 1 - 1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)