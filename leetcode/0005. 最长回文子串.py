class Solution:
    # 法一: 动态规划
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0: return ""
        dp = [[False for _ in range(n)] for _ in range(n)]

        ans = s[-1]
        max_len = 1
        for i in range(n - 1, -1, -1):
            for j in range(i, n, 1):
                if i == j:
                    dp[i][j] = True
                elif j - i == 1:
                    dp[i][j] = s[i] == s[j]
                else:
                    dp[i][j] = s[i] == s[j] and dp[i + 1][j - 1]
                
                if dp[i][j] and j - i + 1 >= max_len:
                    max_len = j - i + 1
                    ans = s[i:j+1]
        return ans


    # 法二: 双指针
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n <= 1: return s
        ans = s[0]
        for i in range(n - 1):
            sub_str1 = self.helper(s, i, i)
            sub_str2 = self.helper(s, i, i + 1)
            sub_str = sub_str1 if len(sub_str1) > len(sub_str2) else sub_str2
            ans = ans if len(ans) > len(sub_str) else sub_str
        return ans

    def helper(self, s, i, j):
        n = len(s)
        if s[i] == s[j]:
            while i > 0 and j < n - 1 and s[i - 1] == s[j + 1]:
                i, j = i - 1, j + 1
            return s[i:j + 1]
        return ""
