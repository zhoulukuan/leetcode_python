class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        circle = [[False for _ in range(n)] for _ in range(n)]
        # 获取s从i到j是否是回文串
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if i == j:
                    circle[i][j] = True
                elif (s[i] == s[j]) and (j - i == 1 or circle[i+1][j-1]):
                    circle[i][j] = True
        
        # dp数组,计算0~i位置的最小切割
        dp = [n -1] * n
        for i in range(n):
            # 如果是回文串,不需要切割,次数为0
            if circle[0][i]:
                dp[i] = 0
            else:
                # 如果不是回文串,可以在0~i的任一位置切割,转化成0~j,j+1~i两段
                # 若j+1~i是回文,则当前需要切割的次数为dp[j]+1
                # 若j+1~i不是回文串,不需要考虑,举例:i=8,j=4
                # 那么dp[8]等于dp[4]+5~8这个区间转化成回文串最小需要切割若干次,最后一次位置是x
                # 则必然有x+1~8的区间是回文串,dp[8]=dp[x]+1,也就是说,随着j从4增加到x,后者会涵盖之前后一个区间不为回文串的情况!
                for j in range(i):
                    if circle[j+1][i]:
                        dp[i] = min(dp[i], dp[j] + 1)
        return dp[n - 1]
