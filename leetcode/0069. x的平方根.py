class Solution:
    def mySqrt(self, x: int) -> int:
        lo, hi = 0, x
        while lo < hi:
            mid = hi - (hi - lo) // 2
            num = mid * mid
            if num == x:
                return mid
            elif num < x:
                lo = mid
            else:
                hi = mid - 1
        return lo
