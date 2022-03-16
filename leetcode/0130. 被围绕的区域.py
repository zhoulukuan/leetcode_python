from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        for i in range(m):
            self.helper(i, 0, board, m, n)
            self.helper(i, n - 1, board, m, n)
        for j in range(n):
            self.helper(0, j, board, m, n)
            self.helper(m - 1, j, board, m, n)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'Y':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'

    def helper(self, x, y, board, m, n):
        if board[x][y] != 'O':
            return
        q = deque()
        q.append((x, y))
        while q:
            x, y = q.popleft()
            board[x][y] = 'Y'
            for dx, dy in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < m and 0 <= new_y < n and board[new_x][new_y] == 'O':
                    board[new_x][new_y] = 'Y'
                    q.append((new_x, new_y))
