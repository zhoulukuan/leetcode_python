class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        arr.sort()
        # 截断的可能最大值等于数组最大值,最小可能值是0
        # 在数组前补零可以保证结果必然在数组范围中
        arr = [0] + arr
        n = len(arr)
        # 数组和用于加快计算
        arr_sum = [num for num in arr]
        for i in range(1, len(arr_sum)):
            arr_sum[i] += arr_sum[i - 1]
        
        # 二分查找法
        # hi:>, lo:<=
        lo, hi = 0, arr[-1]
        while lo < hi:
            mid = lo + (hi - lo) // 2
            curr_sum = self.get_sum(arr, arr_sum, mid)
            if curr_sum <= target:
                lo = mid + 1
            else:
                hi = mid
        lo = hi - 1

        lo_sum = self.get_sum(arr, arr_sum, lo)
        hi_sum = self.get_sum(arr, arr_sum, hi)
        if abs(lo_sum - target) <= abs(hi_sum - target):
            return lo
        else:
            return hi


    def binary_search(self, arr, target):
        if target < arr[0] or target > arr[-1]:
            return -1
        lo, hi = 0, len(arr)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if arr[mid] <= target:
                lo = mid + 1
            else:
                hi = mid
        return lo

    def get_sum(self, arr, arr_sum, value):
        index = self.binary_search(arr, value)
        curr_sum = arr_sum[index - 1] + (len(arr) - index) * value
        return curr_sum
