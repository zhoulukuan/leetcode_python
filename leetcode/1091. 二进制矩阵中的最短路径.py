from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] != 0 or grid[n - 1][n - 1] != 0: return -1

        q = deque()
        q.append((0, 0))
        curr_level = 1
        while q:
            curr_num = len(q)
            for _ in range(curr_num):
                x, y = q.popleft()
                if x == n - 1 and y == n - 1:
                    return curr_level
                for dx, dy in ((-1, -1), (-1, 0), (0, -1), (-1, 1),
                            (1, 1), (1, 0), (0, 1), (1, -1)):
                    new_x, new_y = x + dx, y + dy
                    if 0 <= new_x < n and 0 <= new_y < n and grid[new_x][new_y] == 0:
                        q.append((new_x, new_y))
                        grid[new_x][new_y] = 2
            curr_level += 1
        return -1
