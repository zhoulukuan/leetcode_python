class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        if n < 1 or target < nums[0] or target > nums[-1]: return [-1, -1]
        
        lo, hi = 0, n
        while lo < hi:
            mid = (lo + hi) >> 1
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid
        p1 = lo
        if nums[p1] != target:
            return [-1, -1]

        lo, hi = 0, n
        while lo < hi:
            mid = (lo + hi) >> 1
            if nums[mid] <= target:
                lo = mid + 1
            else:
                hi = mid
        p2 = lo - 1
        return [p1, p2]
