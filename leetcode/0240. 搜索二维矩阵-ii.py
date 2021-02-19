class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        if n == 0: return False
        m = len(matrix[0])
        if m == 0: return False

        # 沿对角线搜索
        row = 0
        col = m - 1
        while row < n and col >= 0:
            num = matrix[row][col]
            if num == target:
                return True
            elif num < target:
                row += 1
            else:
                col -= 1
        return False
