class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        lo, hi = 0, 0
        window = nums[0]
        ans = len(nums) + 1
        while hi < len(nums):
            # print("%d" % (ans))
            if window >= s:
                ans = min(ans, hi - lo + 1)
            if window < s or lo == hi:
                hi += 1
                if hi == len(nums): break
                window += nums[hi]
            else:
                window -= nums[lo]
                lo += 1
        return ans if ans <= len(nums) else 0
