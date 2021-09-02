class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [1, 1] + [0 for _ in range(n)]
        s = '99' + s

        for i in range(2, n + 2):
            if s[i] != '0':
                dp[i] += dp[i - 1]
            if s[i - 1] == '1' or (s[i - 1] == '2' and s[i] <= '6'):
                dp[i] += dp[i - 2]
        return dp[-1]
