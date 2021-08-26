class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        s = [c for c in s]
        dp = [[False for _ in range(n)] for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(n):
                if i == j:
                    dp[i][j] = True
                elif s[i] == s[j]:
                    if i + 1 == j or (i + 1 < j and dp[i + 1][j - 1]):
                        dp[i][j] = True
        if dp[0][n - 1]: return 0

        # 动态规划
        cut = [0 for _ in range(n)]
        for i in range(n):
            # 如果0~i是回文,不需要切割,次数为0
            if dp[0][i]:
                cut[i] = 0
            else:
                max_time = i
                # 如果0~i不是回文,可以通过如下途径变成回文
                # 对于0<=j<i, 可以分为0~j和j+1~i两段,如果j+1~i是回文,则可以通过0~j状态进行状态转移
                # 备注: 不需要考虑j+1~i不是回文的情况,因为j变大的时候会覆盖这种情况
                for j in range(i):
                    if dp[j + 1][i]:
                        max_time = min(max_time, cut[j] + 1)
                cut[i] = max_time
        return cut[-1]
