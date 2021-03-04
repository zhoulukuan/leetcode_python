class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        if n < 4: return []
        
        nums.sort()
        ans = []

        p1 = 0
        while p1 < n - 3:
            if (nums[p1] * 4 > target): break
            p2 = p1 + 1
            while p2 < n - 2:
                if (nums[p1] + nums[p2] * 3 > target): break
                p3, p4 = p2 + 1, n - 1
                while p3 < p4:
                    curr = nums[p1] + nums[p2] + nums[p3] + nums[p4]
                    if curr == target:
                        ans.append([nums[p1], nums[p2], nums[p3], nums[p4]])
                        p3, p4 = p3 + 1, p4 - 1
                        while p3 < p4 and nums[p3] == nums[p3 - 1]: p3 += 1
                        while p3 < p4 and nums[p4] == nums[p4 + 1]: p4 -= 1
                    elif curr > target:
                        p4 -= 1
                        while p3 < p4 and nums[p4] == nums[p4 + 1]: p4 -= 1
                    else:
                        p3 += 1
                        while p3 < p4 and nums[p3] == nums[p3 - 1]: p3 += 1
                    if (nums[p4] * 4 < target): break
                p2 += 1
                while p2 < n - 2 and nums[p2] == nums[p2 - 1]: p2 += 1
            p1 += 1
            while p1 < n - 3 and nums[p1] == nums[p1 - 1]: p1 += 1

        return ans
