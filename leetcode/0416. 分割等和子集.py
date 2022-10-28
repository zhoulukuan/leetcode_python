class Solution:
    def canPartition(self, nums):
        sumValue = sum(nums)
        if sumValue % 2 == 1:
            return False

        target = sumValue // 2
        dp = [False for _ in range(target + 1)]
        dp[0] = True

        for num in nums:
            for i in range(target, -1, -1):
                if i >= num:
                    dp[i] = dp[i] or dp[i - num]
        return dp[target]
