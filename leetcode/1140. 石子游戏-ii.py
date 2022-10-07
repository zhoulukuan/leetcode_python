class Solution:
    # 核心思想:
    # 如果是从前往后推是没办法推断的,因为当前收益取决于后续的状态,但是如果从后往前推可以
    # 最大收益取决于两个状态,1个是当前位置i,1个是当前的M值

    # 当i+2M>=n,代表剩下的石子可以全部拿走
    # 当i+2M<n,则需要循环迭代,设当前拿走的石子数为x,那么先拿的人拿走x个石子后,剩下的人开始拿时候的状态就是从i+x开始拿,M值更新为max(x,M)
    # 剩下石子减去i+x和max(x,M)状态的最大值(即后拿的人最多可以分走的收益),就是先拿的人的收益

    # 法一: 动态规划
    def stoneGameII(self,  piles):
        n = len(piles)
        dp = [[0 for _ in range(2 * n)] for _ in range(n)]

        suff = [p for p in piles]
        for i in range(n - 2, -1, -1):
            suff[i] = piles[i] + suff[i + 1]

        for i in range(n - 1, -1, -1):
            for j in range(2 * n - 1, 0, -1):
                if i + 2 * j > n - 1:
                    dp[i][j] = suff[i]
                else:
                    for x in range(1, 2 * j + 1):
                        dp[i][j] = max(dp[i][j], suff[i] - dp[i+x][max(x,j)])
        return dp[0][1]

    # 法二: 记忆化搜索
    def stoneGameII(self,  piles):
        n = len(piles)
        memo = dict()
        suff = [p for p in piles]
        for i in range(n - 2, -1, -1):
            suff[i] = piles[i] + suff[i + 1]

        def dfs(i, M):
            if (i, M) in memo:
                return memo[(i, M)]
            if i >= n:
                v = 0
            elif i + 2 * M > n - 1:
                v = suff[i]
            else:
                v = 0
                for x in range(1, 2 * M + 1):
                    v = max(v, suff[i] - dfs(i + x, max(x, M)))
            memo[(i, M)] = v
            return v
        return dfs(0, 1)
