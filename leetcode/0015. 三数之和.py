class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        if n < 3: return ans
        
        nums.sort()
        for i in range(n - 2):
            n1 = nums[i]
            # [a,b,c],a为零,由于排序过,和必然大于零
            if n1 > 0: break
            # 确保不同解的a1,a2.....等等不是重复的
            if i > 0 and n1 == nums[i - 1]: continue

            lo, hi = i + 1, len(nums) - 1
            while lo < hi:
                if nums[lo] + nums[hi] < -n1:
                    lo += 1
                elif nums[lo] + nums[hi] > -n1:
                    hi -= 1
                else:
                    ans.append([n1, nums[lo], nums[hi]])
                    lo += 1
                    hi -= 1
                    # 确保b和c不重复
                    while lo < hi and nums[lo] == nums[lo - 1]: lo += 1
                    while hi > lo and nums[hi] == nums[hi + 1]: hi -= 1
        return ans
