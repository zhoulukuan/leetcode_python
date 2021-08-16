class Solution:
    def findLengthOfLCIS(self, nums) -> int:
        n = len(nums)
        dp = [1 for _ in range(n)]
        ans = 1
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                dp[i] = dp[i - 1] + 1
                ans = max(ans, dp[i])
