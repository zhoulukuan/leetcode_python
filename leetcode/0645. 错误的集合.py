class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            while nums[i] != i + 1 and nums[i] != nums[nums[i] - 1]:
                j = nums[i] - 1
                nums[i], nums[j] = nums[j], nums[i]
        
        ans = [0, 0]
        for i in range(n):
            if nums[i] != i + 1:
                ans[1] = i + 1
                ans[0] = nums[i]
        return ans
