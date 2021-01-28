class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # 核心思想: <=lo的区间均为上坡,>=hi的区间均为下坡
        # Lo和hi重合的时候是峰值
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] > nums[mid + 1]:
                hi = mid
            else:
                lo = mid + 1
        return lo
