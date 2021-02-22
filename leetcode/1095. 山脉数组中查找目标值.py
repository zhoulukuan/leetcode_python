# 法一:递归+二分法,有序的一边用二分查找,山峰的一边用递归
class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n = mountain_arr.length()
        return self._find_from_mountain_array(target, mountain_arr, 0, n - 1,
                                              mountain_arr.get(0), mountain_arr.get(n - 1))

    def _find_from_mountain_array(self, target, mountain_arr, lo, hi, vlo, vhi):
        # 递归终止状态
        if lo > hi: return -1
        if lo == hi: return lo if vlo == target else -1
        
        # 函数运算过程
        mid = lo + (hi - lo) // 2
        vmid = mountain_arr.get(mid)
        vnext = mountain_arr.get(mid + 1)
        if vmid < vnext:
            i = self._find_from_monotonic_array(target, mountain_arr, lo, mid, vlo, vmid, True)
            if i != -1: return i
            return self._find_from_mountain_array(target, mountain_arr, mid + 1, hi, vnext, vhi)
        else:
            i = self._find_from_mountain_array(target, mountain_arr, lo, mid, vlo, vmid)
            if i != -1: return i
            return self._find_from_monotonic_array(target, mountain_arr, mid + 1, hi, vnext, vhi, False)

    def _find_from_monotonic_array(self, target, mountain_arr, lo, hi, vlo, vhi, increase):
        # 边界值处理,确保target在[lo,hi]的区间内
        if self._compare(target, vlo, increase) or self._compare(vhi, target, increase):
            return -1

        while lo <= hi:
            mid = lo + (hi - lo) // 2
            vmid = mountain_arr.get(mid)
            if vmid == target:
                return mid

            if self._compare(vmid, target, increase):
                lo = mid + 1
            else:
                hi = mid - 1
        return -1

    def _compare(self, n1, n2, increase):
        if increase:
            return n1 < n2
        else:
            return n1 > n2

# 法二: 先找峰值然后分两段求解
class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n = mountain_arr.length()
        index = self._find_mountain(mountain_arr, 0, n - 1)
        v1 = mountain_arr.get(0)
        vm = mountain_arr.get(index)
        v2 = mountain_arr.get(n - 1)
        if v1 <= target <= vm:
            i = self._find_from_monotonic_array(target, mountain_arr, 0, index, True)
            if i != -1: return i
        if v2 <= target <= vm:
            i = self._find_from_monotonic_array(target, mountain_arr, index + 1, n - 1, False)
            if i != -1: return i
        return -1

    def _find_mountain(self, mountain_arr, lo, hi):
        while lo < hi:
            mid = lo + (hi - lo) // 2
            vmid = mountain_arr.get(mid)
            vnext = mountain_arr.get(mid + 1)
            if vmid < vnext:
                lo = mid + 1
            else:
                hi = mid
        return lo


    def _find_from_monotonic_array(self, target, mountain_arr, lo, hi, increase):
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            vmid = mountain_arr.get(mid)
            if vmid == target:
                return mid

            if self._compare(vmid, target, increase):
                lo = mid + 1
            else:
                hi = mid - 1
        return -1

    def _compare(self, n1, n2, increase):
        if increase:
            return n1 < n2
        else:
            return n1 > n2
