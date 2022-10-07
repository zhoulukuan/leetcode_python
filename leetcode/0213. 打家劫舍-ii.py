class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        else:
            return max(self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums):
        if len(nums) <= 2:
            return max(nums)
        a = nums[0]
        b = max(nums[1], nums[0])
        ans = b
        for i in range(2, len(nums)):
            curr = max(a + nums[i], b)
            a, b = b, curr
            ans = max(ans, curr)
        return ans
