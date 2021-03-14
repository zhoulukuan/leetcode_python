class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        if m > 0: n = len(matrix[0])
        flag1, flag2 = False, False
        for i in range(m):
            if matrix[i][0] == 0:
                flag1 = True
                break
        for j in range(n):
            if matrix[0][j] == 0:
                flag2 = True
                break
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if flag1:
            for i in range(m): matrix[i][0] = 0
        if flag2:
            for j in range(n): matrix[0][j] = 0
