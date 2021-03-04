class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n < 3: return 0

        ans = sum(nums[:3])
        gap = abs(target - ans)
        nums.sort()
        index = 0

        while index < n - 2:
            lo, hi = index + 1, n - 1
            while lo < hi:
                curr = nums[lo] + nums[hi] + nums[index]
                if curr == target:
                    return target
                elif curr > target:
                    hi -= 1
                    while lo < hi and nums[hi] == nums[hi + 1]: hi -= 1
                else:
                    lo += 1
                    while lo < hi and nums[lo] == nums[lo - 1]: lo += 1
                if abs(curr - target) < gap:
                    gap = abs(curr - target)
                    ans = curr
            index += 1
            while index < n and nums[index] == nums[index - 1]: index += 1
        return ans
