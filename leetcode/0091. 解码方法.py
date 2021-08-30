class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        if n == 0: return 0
        if n == 1: return int(s != '0')

        s = [c for c in s]
        dp = [0 for _ in range(n + 2)]
        s = ['9', '9'] + s
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 2):
            flag = self.helper(s[i - 1:i+1])
            if s[i] == '0':
                if not flag:
                    return 0
                else:
                    dp[i] = dp[i - 2]
            else:
                if not flag:
                    dp[i] = dp[i - 1]
                else:
                    dp[i] = dp[i - 1] + dp[i - 2]

        return dp[-1]

    def helper(self, sub_str):
        if len(sub_str) == 1:
            return sub_str[0] != '0'
        else:
            return (sub_str[0] == '1') or (sub_str[0] == '2' and sub_str[1] <= '6')
