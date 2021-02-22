class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] == nums[mid + 1]:  # lo < hi所以mid+1必定存在
                second_half = hi - mid + 1
                if second_half % 2 == 1:
                    lo = mid
                else:
                    hi = mid - 1
            elif nums[mid] == nums[mid - 1]:    # lo和hi的闭区间元素数量为奇数,所以mid-1必定存在,不会出现hi=lo+1的情况
                first_half = mid - lo + 1
                if first_half % 2 == 1:
                    hi = mid
                else:
                    lo = mid + 1
            else:
                return nums[mid]
        return nums[lo]
