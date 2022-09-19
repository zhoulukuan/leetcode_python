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
    
class Solution:
    def jump(self, nums) -> int:
        n = len(nums)
        if n == 1: return 0

        curr = 0
        next = 0
        step = 0
        i = 0
        while i < n:
            while i <= curr:
                next = max(next, i + nums[i])
                if next >= n - 1:
                    return step + 1
                i += 1
            curr = next
            next = 0
            step += 1
        return -1
