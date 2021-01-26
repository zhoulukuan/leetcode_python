class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lo = 0
        hi = len(nums)
        if hi == 0: return [-1, -1]
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid
        if lo < len(nums) and nums[lo] == target:
            start = lo
        else:
            return [-1, -1]

        lo = 0
        hi = len(nums)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] <= target:
                lo = mid + 1
            else:
                hi = mid
        end = lo - 1

        return [start, end]
