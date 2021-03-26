from collections import deque
class Solution:
    def numIslands(self, grid) -> int:
        m = len(grid)
        if m == 0: return 0
        n = len(grid[0])
        if n == 0: return 0

        ans = 0
        queue = deque()
        flag = [[True for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if flag[i][j] and grid[i][j] == '1':
                    ans += 1
                    self.helper(flag, i, j, queue, m, n, grid)
                flag[i][j] = False
        return ans

    def helper(self, flag, i, j, queue, m, n, grid):
        queue.append([i, j])
        while len(queue) > 0:
            i, j = queue.popleft()
            if 0 <= i < m and 0 <= j < n and flag[i][j] and grid[i][j] == '1':
                flag[i][j] = False
                queue.append([i - 1, j])
                queue.append([i + 1, j])
                queue.append([i, j - 1])
                queue.append([i, j + 1])
