class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = []
        index = 0

        while index < n - 2:
            if nums[index] > 0: break
            lo, hi = index + 1, n - 1
            while lo < hi:
                curr = nums[lo] + nums[hi] + nums[index]
                if curr == 0:
                    ans.append([nums[index], nums[lo], nums[hi]])
                    lo, hi = lo + 1, hi - 1
                    while lo < hi and nums[lo] == nums[lo - 1]: lo += 1
                    while lo < hi and nums[hi] == nums[hi + 1]: hi -= 1
                elif curr > 0:
                    hi -= 1
                    while lo < hi and nums[hi] == nums[hi + 1]: hi -= 1
                else:
                    lo += 1
                    while lo < hi and nums[lo] == nums[lo - 1]: lo += 1
            index += 1
            while index < n and nums[index] == nums[index - 1]: index += 1
        return ans
