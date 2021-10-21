class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        lo, hi = 0, m
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if matrix[mid][0] <= target:
                lo = mid + 1
            else:
                hi = mid
        if lo == 0:
            return False
        else:
            row = lo - 1

        lo, hi = 0, n
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if matrix[row][mid] < target:
                lo = mid + 1
            else:
                hi = mid
        return True if lo < n and matrix[row][lo] == target else False
