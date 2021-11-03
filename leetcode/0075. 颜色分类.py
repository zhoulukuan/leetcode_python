class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lo, hi = 0, len(nums)
        index = 0
        while index < hi:
            if nums[index] == 0:
                nums[index], nums[lo] = nums[lo], nums[index]
                lo += 1
                index += 1
            elif nums[index] == 2:
                hi -= 1
                nums[hi], nums[index] = nums[index], nums[hi]
            else:
                index += 1
