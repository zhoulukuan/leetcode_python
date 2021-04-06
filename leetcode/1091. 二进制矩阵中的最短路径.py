from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        surrounds = [[-1, 0], [1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]
        queue = deque()
        visited = [[False for _ in range(n)] for _ in range(m)]

        if grid[0][0] != 0: return -1
        level = 1
        queue.append([0, 0])
        visited[0][0] = True
        while queue:
            size = len(queue)
            for _ in range(size):
                x, y = queue.popleft()
                if x == m - 1 and y == n - 1: return level
                for dx, dy in surrounds:
                    new_x, new_y = x + dx, y + dy
                    if 0 <= new_x < m and 0 <= new_y < n and visited[new_x][new_y] == False and grid[new_x][new_y] == 0:
                        queue.append([new_x, new_y])
                        visited[new_x][new_y] = True
            level += 1
        return -1
