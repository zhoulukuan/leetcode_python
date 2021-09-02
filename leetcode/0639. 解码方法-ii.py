class Solution:
    def numDecodings(self, s: str) -> int:
        MOD = 10 ** 9 + 7
        n = len(s)
        dp = [1, 1] + [0 for _ in range(n)]
        s = '99' + s

        for i in range(2, n + 2):
            if s[i] == '*':
                dp[i] += dp[i - 1] * 9
                if s[i - 1] == '1' or s[i - 1] == '*':
                    dp[i] += dp[i - 2] * 9
                if s[i - 1] == '2' or s[i - 1] == '*':
                    dp[i] += dp[i - 2] * 6
            else:
                if s[i] != '0':
                    dp[i] += dp[i - 1]
                if s[i - 1] == '1' or (s[i - 1] == '2' and '0' <= s[i] <= '6'):
                    dp[i] += dp[i - 2]
                if s[i - 1] == '*':
                    if s[i] <= '6': dp[i] += dp[i - 2] * 2
                    else: dp[i] += dp[i - 2]
            dp[i] = dp[i] % MOD
        return dp[-1]
