class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1 = len(word1)
        n2 = len(word2)
        dp = [[0 for _ in range(n2 + 1)] for _ in range(n1 + 1)]
        word1 = ['#'] + [c for c in word1]
        word2 = ['#'] + [c for c in word2]

        for i in range(n1 + 1):
            for j in range(n2 + 1):
                if i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                else:
                    if word1[i] == word2[j]:
                        dp[i][j] = min(dp[i-1][j-1], dp[i-1][j] + 1, dp[i][j-1]+1)
                    else:
                        dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
        return dp[-1][-1]
