from collections import deque
class Solution:
    def shortestPath(self, grid, k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        queue = deque()
        directions = [[0, 1],[0, -1],[1, 0],[-1,0]]
        # 记录的时候要添加k+1这个维度,否则就会出现
        # 某个点被消除次数更多的路径访问过了,导致消除次数更少的路径无法访问该点从而得不到正确解的情况
        visited = [[[False for _ in range(k + 1)] for _ in range(n)] for _ in range(m)]


        visited[0][0][0] = True
        queue.append([0, 0, 0])

        level = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                x, y, remove = queue.popleft()
                if x == m - 1 and y == n - 1: return level
                for dx, dy in directions:
                    new_x, new_y = x + dx, y + dy
                    if 0 <= new_x < m and 0 <= new_y < n:
                        if grid[new_x][new_y] == 1:
                            if remove + 1 > k or visited[new_x][new_y][remove + 1]: continue
                            queue.append([new_x, new_y, remove + 1])
                            visited[new_x][new_y][remove + 1] = True
                        else:
                            if visited[new_x][new_y][remove]: continue
                            queue.append([new_x, new_y, remove])
                            visited[new_x][new_y][remove] = True
            level += 1
        return -1
