import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        h = [(matrix[i][0], i, 0) for i in range(n)]
        heapq.heapify(h)

        for _ in range(k - 1):
            _, r, c = heapq.heappop(h)
            if c + 1 < n:
                heapq.heappush(h, (matrix[r][c + 1], r, c + 1))
        ans, _, _ = heapq.heappop(h)
        return ans
