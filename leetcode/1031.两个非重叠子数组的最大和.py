class Solution:
    def maxSumTwoNoOverlap(self, nums, firstLen: int, secondLen: int) -> int:
        n = len(nums)
        if n <= firstLen + secondLen: return sum(nums)

        dp_pre_first = [float('-inf')] * n
        dp_pre_second = [float('-inf')] * n
        dp_suff_first = [float('-inf')] * n
        dp_suff_second = [float('-inf')] * n

        dp_pre_first[firstLen - 1] = sum(nums[:firstLen])
        curr = dp_pre_first[firstLen - 1]
        for i in range(firstLen, n):
            curr = curr + nums[i] - nums[i - firstLen]
            dp_pre_first[i] = max(curr, dp_pre_first[i - 1])

        dp_pre_second[secondLen - 1] = sum(nums[:secondLen])
        curr = dp_pre_second[secondLen - 1]
        for i in range(secondLen, n):
            curr = curr + nums[i] - nums[i - secondLen]
            dp_pre_second[i] = max(curr, dp_pre_second[i - 1])

        dp_suff_first[n - firstLen] = sum(nums[n - firstLen:])
        curr = dp_suff_first[n - firstLen]
        for i in range(n - firstLen - 1, -1, -1):
            curr = curr + nums[i] - nums[i + firstLen]
            dp_suff_first[i] = max(curr, dp_suff_first[i + 1])

        dp_suff_second[n - secondLen] = sum(nums[n - secondLen:])
        curr = dp_suff_second[n - secondLen]
        for i in range(n - secondLen - 1, -1, -1):
            curr = curr + nums[i] - nums[i + secondLen]
            dp_suff_second[i] = max(curr, dp_suff_second[i + 1])

        ans = 0
        for i in range(firstLen - 1, n - secondLen):
            ans = max(dp_pre_first[i] + dp_suff_second[i + 1], ans)
        for i in range(secondLen - 1, n - firstLen):
            ans = max(dp_pre_second[i] + dp_suff_first[i + 1], ans)
        return ans
