class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            # 若已经有序,直接返回首个元素的值
            if nums[lo] <= nums[hi]:
                return nums[lo]

            # 若仍然是旋转数组,则
            mid = lo + (hi - lo) // 2
            if nums[lo] <= nums[mid]:
                # lo~mid段有序,则直接舍弃,包含了lo=mid的情况
                # 可能仍然是旋转数组,或者直接导致有序
                lo = mid + 1
            else:
                # 取mid-1的话,会导致旋转段只有一个元素的时候得不到正解
                hi = mid
        return -1
