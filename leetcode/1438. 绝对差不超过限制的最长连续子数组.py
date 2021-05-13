from collections import deque
class Solution:
    def longestSubarray(self, nums, limit: int) -> int:
        queMax = deque()
        queMin = deque()
        ans = left = right = 0
        n = len(nums)

        while right < n:
            while queMax and queMax[-1] < nums[right]:
                queMax.pop()
            while queMin and queMin[-1] > nums[right]:
                queMin.pop()

            queMax.append(nums[right])
            queMin.append(nums[right])

            while queMax and queMin and queMax[0] - queMin[0] > limit:
                if queMax[0] == nums[left]: queMax.popleft()
                if queMin[0] == nums[left]: queMin.popleft()
                left += 1

            ans = max(ans, right - left + 1)
            right += 1
        return ans
