class Solution:
    def minDistance(self, word1, word2):
        m = len(word1)
        n = len(word2)
        if m * n == 0:
            return m + n

        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j

        # 递推方程:word1[:i]到word2[:j]需要的最少转化次数
        # 要点1: dp[i][j]由dp[a][b]递推,其中只用考虑a<=i和b<=j的情况,不需要考虑a>i或b>j
        # 因为word1插入一个字母和word2删除一个字母是等价的,反之亦然
        # 例如从dp[a][j]递推dp[i][j],a>i; a转化到i需要word1删除若干个字符,则可以转化word2增加若干个字符,即等价dp[i][j-(a-i)]递推dp[i][j]
        # 要点2: dp[i][j]可以只由dp[i-1][j-1]、dp[i][j-1]和dp[i-1][j]递推
        # 因为只有两种情况,第一种是word1和word2的最后一个字符都不需要操作,即保留,那么dp[i][j]和dp[i-1][j-1]存在关系
        # 第二种是word1和word2中有1个以上最后一个字符需要转化,那么由于操作不区分先后顺序,因此可以把操作最后一位放到最后,即和dp[i][j-1]和dp[i-1][j]存在关系
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # 三种操作
                # 替换,dp[i - 1][j - 1]递推,若两个字符串当前最后一个字符相等,可以省下一步替换操作,否则操作数+1
                # word1新增, word1[:i-1] -> word2[j], 然后补1位, 即dp[i-1][j] + 1
                # word2新增, word1[:i] -> word2[j-1], 然后补1位, 即dp[i][j-1] + 1
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                else:
                    dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1])
        return dp[-1][-1]
