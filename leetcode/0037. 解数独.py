class Solution:
    def solveSudoku(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        sr = [set() for _ in range(9)]
        sc = [set() for _ in range(9)]
        sm = [[set() for _ in range(3)] for _ in range(3)]
        remain = []

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    remain.append((i, j))
                else:
                    sr[i].add(board[i][j])
                    sc[j].add(board[i][j])
                    sm[i // 3][j // 3].add(board[i][j])

        n = len(remain)

        def backtracking(i):
            if i == n:
                return True
            for num in range(1, 10):
                char = str(num)
                row, col = remain[i]
                if char not in sr[row] and char not in sc[col] and char not in sm[row // 3][col // 3]:
                    board[row][col] = char
                    sr[row].add(char)
                    sc[col].add(char)
                    sm[row // 3][col // 3].add(char)
                    if backtracking(i + 1): return True
                    sm[row // 3][col // 3].remove(char)
                    sr[row].remove(char)
                    sc[col].remove(char)
                    board[row][col] = '.'

        backtracking(0)
