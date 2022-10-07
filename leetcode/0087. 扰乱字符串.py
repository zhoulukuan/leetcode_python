class Solution:
    def isScramble(self, s1, s2):
        n = len(s1)
        # 构造dp
        # 定义:dp[i][j][k]从s1的i位置,s2的j位置开始,长度为k的字符串是否可扰乱
        dp = [[[False for _ in range(n + 1)] for _ in range(n)] for _ in range(n)]

        # 初始化,若[i,j]位置字符相等,则从各自的位置开始长度为1的字符串可扰乱
        for i in range(n):
            for j in range(n):
                if s1[i] == s2[j]:
                    dp[i][j][1] = True

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                for k in range(2, n + 1):
                    # 从s1的i位置,s2的j位置开始长度为k的字符串可扰乱有2种可能
                    # 两个字符串都是从前向后截取的,则对于1<=x<k,可以分为x和k-x两段
                    # 必须存在dp[i][j][x]和dp[i+x][j+x][k-x]同时可扰乱
                    # s1从前向后截取而s2从后向前截取的,则对于1<=x<k,可以分为x和k-x两段
                    # 必须存在dp[i+x][j][k-x]和dp[i][j+k-x][x]同时可扰乱
                    for x in range(1, k):
                        if i+x < n and j+x < n and dp[i][j][x] and dp[i+x][j+x][k-x]:
                            dp[i][j][k] = True
                            break
                        if i+x < n and j+k-x < n and dp[i][j+k-x][x] and dp[i+x][j][k-x]:
                            dp[i][j][k] = True
                            break
        return dp[0][0][n]
