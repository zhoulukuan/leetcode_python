class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        n = len(s1)
        if n != len(s2): return False

        dp = [[[False for _ in range(n + 1)] for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if s1[i] == s2[j]:
                    dp[i][j][1] = True

        for k in range(2, n + 1):
            for i in range(n + 1 - k):
                for j in range(n + 1 - k):
                    for curr in range(1, k):
                        if dp[i][j][curr] and dp[i + curr][j + curr][k - curr]:
                            dp[i][j][k] = True
                            break
                        if dp[i][j + k - curr][curr] and dp[i + curr][j][k - curr]:
                            dp[i][j][k] = True
                            break
        return dp[0][0][n]
