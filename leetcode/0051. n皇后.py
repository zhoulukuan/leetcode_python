class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n < 1: return None
        ans = []
        board = [['.' for _ in range(n)] for _ in range(n)]
        sc = set()
        sv = set()

        def is_valid(board, row, col, sc, sv):
            if col in sc:
                return False

            if row + col in sv:
                return False

            minV, maxV = min(row, col), max(row, col)
            for i in range(1, n - maxV):
                if board[row + i][col + i] == 'Q':
                    return False

            for i in range(1, minV + 1):
                if board[row - i][col - i] == 'Q':
                    return False
            return True

        def backtracking(board, row, sc, sv):
            if row == n:
                ans.append([''.join(line) for line in board])
                return
            for i in range(n):
                if is_valid(board, row, i, sc, sv):
                    board[row][i] = 'Q'
                    sc.add(i)
                    sv.add(row + i)
                    backtracking(board, row + 1, sc, sv)
                    sv.remove(row + i)
                    sc.remove(i)
                    board[row][i] = '.'

        backtracking(board, 0, sc, sv)
        return ans
