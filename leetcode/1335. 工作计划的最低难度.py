class Solution:
    def minDifficulty(self, jobDifficulty, d: int) -> int:
        INF = 100000
        n = len(jobDifficulty)
        maxV = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(i, n):
                if i == j:
                    maxV[i][j] = jobDifficulty[i]
                else:
                    maxV[i][j] = max(maxV[i][j - 1], jobDifficulty[j])

        dp = [[INF for _ in range(d)] for _ in range(n)]
        for i in range(n):
            for j in range(min(d, i + 1)):
                if j == 0:
                    dp[i][j] = maxV[0][i]
                else:
                    dp[i][j] = INF
                    for k in range(j - 1, i):
                        if dp[k][j - 1] != INF:
                            dp[i][j] = min(dp[k][j - 1] + maxV[k + 1][i], dp[i][j])
        return -1 if dp[-1][-1] == INF else dp[-1][-1]
