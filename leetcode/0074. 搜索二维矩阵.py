class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if m == 0: return False
        n = len(matrix[0])
        if n == 0: return False

        lo, hi = 0, m
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if matrix[mid][0] == target: return True
            if matrix[mid][0] <= target:
                lo = mid + 1
            else:
                hi = mid
        line = lo - 1
        
        lo, hi = 0, n
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if matrix[line][mid] == target: return True
            if matrix[line][mid] < target:
                lo = mid + 1
            else:
                hi = mid
        if lo < n and matrix[line][lo] == target:
            return True
        return False
