class Solution:
    def longestConsecutive(self, nums) -> int:
        if len(nums) == 0: return 0
        origin = set()
        for num in nums:
            origin.add(num)

        ans = 1
        used = set()
        for num in origin:
            if num in used:
                continue
            curr = 0
            while num in origin:
                curr += 1
                num += 1
                used.add(num)
            ans = max(ans, curr)
        return ans
