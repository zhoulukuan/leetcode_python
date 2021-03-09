class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1: return n

        ans = 0
        lo = 0
        while lo < n:
            hi = lo + 1
            while hi < n and nums[hi] == nums[lo]: hi += 1
            nums[ans] = nums[lo]
            ans += 1
            lo = hi
        return ans
