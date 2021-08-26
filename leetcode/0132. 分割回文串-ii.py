class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        s = [c for c in s]
        dp = [[False for _ in range(n)] for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(n):
                if i == j:
                    dp[i][j] = True
                elif s[i] == s[j]:
                    if i + 1 == j or (i + 1 < j and dp[i + 1][j - 1]):
                        dp[i][j] = True
        if dp[0][n - 1]: return 0

        cut = [0 for _ in range(n)]
        for i in range(n):
            if dp[0][i]:
                cut[i] = 0
            else:
                max_time = i
                for j in range(i):
                    if dp[j + 1][i]:
                        max_time = min(max_time, cut[j] + 1)
                cut[i] = max_time
        return cut[-1]
