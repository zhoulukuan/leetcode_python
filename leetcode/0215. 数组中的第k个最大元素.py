class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.helper(nums, 0, len(nums) - 1, k)

    def helper(self, nums, start, end, k):
        if start > end:
            return -1

        value = nums[end]
        boundary = start
        for i in range(start, end):
            if nums[i] < value:
                nums[i], nums[boundary] = nums[boundary], nums[i]
                boundary += 1
        nums[boundary], nums[end] = nums[end], nums[boundary]

        if end - boundary > k - 1:
            return self.helper(nums, boundary + 1, end, k)
        elif end - boundary == k - 1:
            return nums[boundary]
        else:
            return self.helper(nums, start, boundary - 1, k - (end - boundary + 1))
