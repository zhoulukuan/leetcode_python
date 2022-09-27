class Solution:
    def numDecodings(self, s):
        if s[0] == '0':
            return 0

        n = len(s)
        dp = [0 for _ in range(n+1)]
        dp[0] = 1
        dp[1] = 1 if s[0] != '*' else 9
        for i in range(2, n + 1):
            if s[i - 1] == '*':
                dp[i] += dp[i - 1] * 9
            elif '1' <= s[i - 1] <= '9':
                dp[i] += dp[i - 1]

            if s[i - 1] == '*' and s[i - 2] == '*':
                dp[i] += dp[i - 2] * 15
            elif s[i - 1] == '*':
                if s[i - 2] == '1':
                    dp[i] += dp[i - 2] * 9
                elif s[i - 2] == '2':
                    dp[i] += dp[i - 2] * 6
            elif s[i - 2] == '*':
                if s[i - 1] <= '6':
                    dp[i] += dp[i - 2] * 2
                else:
                    dp[i] += dp[i - 2]
            elif 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i - 2]

            dp[i] = dp[i] % (10**9 + 7)
        return dp[-1]
