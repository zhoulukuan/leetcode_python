class Solution:
    def findInMountainArray(self, target: int, mountain_arr) -> int:
        n = mountain_arr.length()
        return self.find(mountain_arr, 0, n - 1, target)

    def find(self, mountain_arr, lo, hi, target):
        while lo < hi:
            mid = (lo + hi) >> 1
            vm = mountain_arr.get(mid)
            nv = mountain_arr.get(mid + 1)
            # lo~mid段递增
            if vm < nv:
                # target若大于vm则不可能在左半段,没有查找的必要
                if target <= vm:
                    index = self.binary_search(mountain_arr, lo, mid + 1, target, 1)
                    if index != -1: return index
                lo = mid + 1
            # mid~hi段递减
            else:
                # 递归
                index = self.find(mountain_arr, lo, mid, target)
                if index != -1: return index
                # target若大于nv则不可能在右半段,没有查找的必要
                if target > nv:
                    return -1
                else:
                    return self.binary_search(mountain_arr, mid + 1, hi + 1, target, -1)
        return lo if mountain_arr.get(lo) == target else -1

    # 带符号的二分法
    def binary_search(self, nums, lo, hi, target, flag):
        n = hi
        while lo < hi:
            mid = (lo + hi) >> 1
            if (nums.get(mid) - target) * flag < 0:
                lo = mid + 1
            else:
                hi = mid

        if lo < n and nums.get(lo) == target:
            return lo
        else:
            return -1
