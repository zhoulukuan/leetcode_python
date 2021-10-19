class Solution:
    def search(self, nums, target: int) -> int:
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = (lo + hi) >> 1
            if nums[lo] < nums[mid]:    # 左半段有序
                if nums[lo] <= target <= nums[mid]:
                    return self.binary_search(nums, lo, mid + 1, target)
                else:
                    lo = mid + 1
            else:                       # 右半段有序
                if nums[mid] <= target <= nums[hi - 1]:
                    return self.binary_search(nums, mid, hi, target)
                else:
                    hi = mid

        if lo < len(nums) and nums[lo] == target:
            return lo
        else:
            return -1

    def binary_search(self, nums, lo, hi, target):
        while lo < hi:
            mid = (lo + hi) >> 1
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid

        if lo < len(nums) and nums[lo] == target:
            return lo
        else:
            return -1
