class Solution:
    def numDecodings(self, s: str) -> int:
        # 可以在前面直接补零,dp直接补1来避开对开头两个字符的复杂判断
        s = '00' + s
        dp = [0 for _ in range(len(s))]
        dp[0] = 1
        dp[1] = 1

        for i in range(2, len(s)):
            # dp[i] = dp[i - 1] + dp[i - 2]
            # i-1项必须满足,当前字符在1~9之间
            if self.range(s[i], 1, 9):
                n1 = dp[i - 1]
            else:
                n1 = 0

            # i-2项必须满足，前一字符和当前字符组成的数字在1~26之间
            if self.range(s[i-1] + s[i], 1, 26):
                n2 = dp[i - 2]
            else:
                n2 = 0

            # 出现0的情况,例如901,则90是没办法解码的，返回0就可以
            if n1 + n2 == 0: return 0
            else: dp[i] = n1 + n2
        return dp[-1]

    def range(self, s, l, h):
        if s[0] == '0': return False
        else: return int(s) <= h and int(s) >= l
