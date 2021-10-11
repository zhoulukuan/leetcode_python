class NumMatrix:
    def __init__(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        accumulate = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(m):
            accumulate[i + 1][1] = accumulate[i][1] + matrix[i][0]
        for j in range(n):
            accumulate[1][j + 1] = accumulate[1][j] + matrix[0][j]
        for i in range(2, m + 1):
            for j in range(2, n + 1):
                accumulate[i][j] = accumulate[i - 1][j] + accumulate[i][j - 1] - accumulate[i - 1][j - 1] + matrix[i - 1][j - 1]
        self.matrix = accumulate

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        v1 = self.matrix[row1][col1]
        v2 = self.matrix[row1][col2 + 1]
        v3 = self.matrix[row2 + 1][col1]
        v4 = self.matrix[row2 + 1][col2 + 1]
        return v4 - v2 - v3 + v1
