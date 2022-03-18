from collections import deque
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = set()

        q = deque()
        q.append((0, 0, 0))
        step = 0
        while q:
            size = len(q)
            for _ in range(size):
                rm, x, y = q.popleft()
                if x == m - 1 and y == n - 1:
                    return step
                for dx, dy in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                    new_x, new_y = x + dx, y + dy
                    if 0 <= new_x < m and 0 <= new_y < n:
                        if grid[new_x][new_y] == 0 and (rm, new_x, new_y) not in visited:
                            q.append((rm, new_x, new_y))
                            visited.add((rm, new_x, new_y))
                        if grid[new_x][new_y] == 1 and rm + 1 <= k and (rm + 1, new_x, new_y) not in visited:
                            q.append((rm + 1, new_x, new_y)) 
                            visited.add((rm + 1, new_x, new_y))
            step += 1
        return -1
