class Solution:
    def maxArea(self, height: List[int]) -> int:
        lo, hi = 0, len(height) - 1
        ans = min(height[lo], height[hi]) * (hi - lo)
        while lo < hi:
            if height[lo] <= height[hi]:
                lo += 1
            else:
                hi -= 1
            t = min(height[lo], height[hi]) * (hi - lo)
            if t >= ans:
                ans = t
        return ans
