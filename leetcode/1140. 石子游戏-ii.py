class Solution:
    def stoneGameII(self, piles) -> int:
        n = len(piles)
        suff_sum = [0 for _ in range(n)]
        suff_sum[-1] = piles[-1]
        for i in range(n - 2, -1, -1):
            suff_sum[i] = suff_sum[i + 1] + piles[i]

        dp = [[0 for _ in range(n + 1)] for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(n + 1):
                if n - i <= 2 * j:
                    dp[i][j] = suff_sum[i]
                else:
                    max_profit = 0
                    for k in range(1, 2 * j + 1):
                        max_profit = max(max_profit, suff_sum[i] - dp[i + k][max(j, k)])
                    dp[i][j] = max_profit
        return dp[0][1]
