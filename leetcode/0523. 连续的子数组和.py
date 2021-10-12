from collections import defaultdict
class Solution:
    def checkSubarraySum(self, nums, k: int) -> bool:
        n = len(nums)
        if n < 2: return False
        accumulate = [0 for _ in range(n)]
        accumulate[0] = nums[0]
        pos = dict()
        pos[accumulate[0] % k] = 0
        pos[0] = -1
        for i in range(1, n):
            accumulate[i] = accumulate[i - 1] + nums[i]
            val = accumulate[i] % k
            if val in pos:
                if i - pos[val] >= 2: return True
            else:
                pos[val] = i

        return False
