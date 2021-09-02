class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n1 = len(s1)
        n2 = len(s2)
        s1 = [c for c in s1]
        s2 = [c for c in s2]
        dp = [[0 for _ in range(n2 + 1)] for _ in range(n1 + 1)]

        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 2 * ord(s1[i - 1])
                else:
                    dp[i][j] = max(dp[i -1][j], dp[i][j - 1])

        ans = 0
        for c in s1:
            ans += ord(c)
        for c in s2:
            ans += ord(c)
        return ans - dp[n1][n2]
