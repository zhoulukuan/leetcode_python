class Solution:
    def maximalSquare(self, matrix) -> int:
        n = len(matrix)
        m = len(matrix[0])
        dp = [[0 for _ in range(m)] for _ in range(n)]

        ans = 0
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == '0':
                    dp[i][j] = 0
                else:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    ans = max(ans, dp[i][j])
        return ans**2
