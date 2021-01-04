class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n <= 1:
            return s
        dp = [[False for _ in range(n)] for _ in range(n)]
        start = 0
        max_len = 1
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if i == j:
                    dp[i][j] = True
                elif s[i] == s[j]:
                    if j - i == 1 or dp[i + 1][j - 1]:
                        dp[i][j] = True
                        if j - i + 1 > max_len:
                            max_len = j - i + 1
                            start = i
                    else:
                        dp[i][j] = False
                else:
                    dp[i][j] = False
        return s[start:start+max_len]
