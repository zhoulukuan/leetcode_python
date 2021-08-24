class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1 = len(text1)
        n2 = len(text2)
        if n1 == 0 or n2 == 0: return 0

        dp = [[0 for _ in range(n2)] for _ in range(n1)]
        text1 = [c for c in text1]
        text2 = [c for c in text2]
        if text1[0] == text2[0]:
            dp[0][0] = 1
        for i in range(1, n1):
            if text1[i] == text2[0]:
                dp[i][0] = 1
            else:
                dp[i][0] = dp[i - 1][0]
        for j in range(1, n2):
            if text1[0] == text2[j]:
                dp[0][j] = 1
            else:
                dp[0][j] = dp[0][j - 1]

        for i in range(1, n1):
            for j in range(1, n2):
                if text1[i] == text2[j]:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1] + 1)
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
        return dp[n1 - 1][n2 - 1]
