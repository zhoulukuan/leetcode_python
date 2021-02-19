import sys
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        n = len(nums)
        ans = sys.maxsize
        for i in range(n):
            l, r = i + 1, n - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < target:
                    l += 1
                    while l < r and nums[l] == nums[l - 1]: l += 1
                elif s > target:
                    r -= 1
                    while l < r and nums[r] == nums[r + 1]: r -= 1
                else:
                    return target
                if abs(s - target) < abs(ans - target):
                    ans = s
        return ans
