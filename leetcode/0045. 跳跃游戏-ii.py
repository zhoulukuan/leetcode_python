class Solution:
    def jump(self, nums) -> int:
        n = len(nums)
        dp = [0 for _ in range(n)]

        for i in range(n):
            max_pos = i + nums[i]
            step = dp[i] + 1
            for j in range(i + 1, min(max_pos + 1, n)):
                if dp[j] == 0:
                    dp[j] = step
        return dp[n - 1]
