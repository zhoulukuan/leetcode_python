class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        # 先锁定所在的行数范围,加快搜索
        lo, hi = 0, m
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if matrix[mid][0] <= target:
                lo = mid + 1
            else:
                hi = mid
        up_bounder = lo

        lo, hi = 0, m
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if matrix[mid][n - 1] < target:
                lo = mid + 1
            else:
                hi = mid
        
        # 不去探索两个边界值直接在矩阵中沿45度对角线搜索也可以
        row, col = lo, n - 1
        while row < up_bounder and col >= 0:
            val = matrix[row][col]
            if val == target:
                return True
            elif val < target:
                row += 1
            else:
                col -= 1
        return False
