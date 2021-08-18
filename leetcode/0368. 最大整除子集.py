class Solution:
    def largestDivisibleSubset(self, nums):
        n = len(nums)
        nums.sort()
        ans = [nums[0]]
        dp = [[] for _ in range(n)]
        for i in range(n):
            dp[i].append(nums[i])
            for j in range(i - 1, -1, -1):
                if nums[i] % dp[j][-1] == 0 and len(dp[j]) + 1 > len(dp[i]):
                    dp[i] = dp[j] + [nums[i]]
            if len(dp[i]) > len(ans): ans = dp[i]
        return ans
