class Solution:
    # 核心思路: 构造dp[i][j]表示开区间i,j内戳破所有气球的最大收益
    def maxCoins(self, nums) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        # 两边填补1,便于处理边界问题
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for j in range(2, n):
            for offset in range(n - j):
                x = offset
                y = j + offset
                max_coin = 0
                # 例如戳破0~6区间内的气球的时候,假如2是最后一个戳破的,那么收益就是：
                # 戳破前半段的收益dp[0][2]+戳破后半段的收益dp[2][6]+戳破2后的收益nums[0]*nums[2]*nums[6]
                for k in range(x + 1, y):
                    curr_coin = dp[x][k] + dp[k][y] + nums[k] * nums[x] * nums[y]
                    max_coin = max(curr_coin, max_coin)
                dp[x][y] = max_coin
        return dp[0][n - 1]
