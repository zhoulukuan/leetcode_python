from collections import deque
class Solution:
    def updateMatrix(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        if m == 0: return None
        n = len(board[0])
        if n == 0: return None

        visited = [[0 for _ in range(n)] for _ in range(m)]
        res = [[0 for _ in range(n)] for _ in range(m)]
        queue = deque()
        for i in range(m):
            for j in range(n):
                if board[i][j] == 0:
                    queue.append([i, j])
                    visited[i][j] = 1

        surround = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        level = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                x, y = queue.popleft()
                if board[x][y] == 1:
                    res[x][y] = level
                for dx, dy in surround:
                    new_x, new_y = x + dx, y + dy
                    if new_x < 0 or new_x >= m or new_y < 0 or new_y >= n or visited[new_x][new_y] == 1:
                        continue
                    queue.append([new_x, new_y])
                    visited[new_x][new_y] = 1
            level += 1
        return res
