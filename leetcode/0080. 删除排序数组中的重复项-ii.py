class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2: return

        ans = 0
        index = 1
        count = 0
        while index < len(nums):
            if nums[index] != nums[ans]:
                ans += 1
                nums[ans] = nums[index]
                index += 1
                count = 0
            else:
                if count == 0:
                    ans += 1
                    nums[ans] = nums[index]
                    index += 1
                    count += 1
                else:
                    index += 1
        return ans + 1
