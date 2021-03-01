class Solution:
    # 统计频率
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        n0, n1 = 0, 0
        for i in range(n):
            if nums[i] == 0:
                n0 += 1
            elif nums[i] == 1:
                n1 += 1
        
        index = 0
        while index < n:
            if index < n0: nums[index] = 0
            elif n0 <= index < n0 + n1: nums[index] = 1
            else: nums[index] = 2
            index += 1
        return nums

    # 遍历，三指针
    def sortColors(self, nums: List[int]) -> None:
        lo, hi = 0, len(nums) - 1
        index = 0
        while index <= hi:
            if nums[index] == 0:
                nums[lo], nums[index] = nums[index], nums[lo]
                lo += 1
                index += 1
            elif nums[index] == 2:
                nums[index], nums[hi] = nums[hi], nums[index]
                hi -= 1
            else:
                index += 1
        return 
