import random
class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        n = len(nums)
        if n < k: return -1
        return self.quickSortHelper(nums, 0, n - 1, k)

    def quickSortHelper(self, nums, lo, hi, k):
        if lo > hi: return -1
        if lo == hi: return nums[lo]
        rand = random.randint(lo, hi + 1)
        nums[rand], nums[hi] = nums[hi], nums[rand]

        val = nums[hi]
        index = lo
        boundary = lo
        while index < hi:
            if nums[index] > val:
                nums[index], nums[boundary] = nums[boundary], nums[index]
                boundary += 1
            index += 1
        nums[index], nums[boundary] = nums[boundary], nums[index]
        if boundary == k - 1:
            return nums[boundary]
        elif boundary < k - 1:
            return self.quickSortHelper(nums, boundary + 1, hi, k)
        else:
            return self.quickSortHelper(nums, lo, boundary, k)
