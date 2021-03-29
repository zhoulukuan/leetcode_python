from collections import deque
class Solution:
    def __init__(self):
        self.m = 0
        self.n = 0
        self.set = set()

    def solve(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        if m == 0: return None
        n = len(board[0])
        if n == 0: return None
        self.m, self.n = m, n

        for i in range(n):
            self.helper(board, 0, i)
        for i in range(n):
            self.helper(board, m - 1, i)
        for j in range(m):
            self.helper(board, j, 0)
        for j in range(m):
            self.helper(board, j, n - 1)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'Y':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'

    # 遍历过的节点要设置条件,否则会产生非常大的计算量
    def helper(self, board, i, j):
        def check(i, j):
            # == 'O'的条件隐含了该点是未遍历过的
            return 0 <= i < self.m and 0 <= j < self.n and board[i][j] == 'O'

        if check(i, j):
            queue = deque()
            queue.append([i, j])
            while len(queue) > 0:
                i, j = queue.popleft()
                board[i][j] = 'Y'
                if check(i - 1, j):
                    board[i - 1][j] = 'Y'
                    queue.append([i - 1, j])
                if check(i + 1, j):
                    board[i + 1][j] = 'Y'
                    queue.append([i + 1, j])
                if check(i, j - 1):
                    board[i][j - 1] = 'Y'
                    queue.append([i, j - 1])
                if check(i, j + 1):
                    board[i][j + 1] = 'Y'
                    queue.append([i, j + 1])
