class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        lo, hi = 1, n
        if isBadVersion(1): return 1

        while lo < hi:
            mid = lo + (hi - lo) // 2
            if not isBadVersion(mid):
                lo = mid + 1
            else:
                hi = mid
        return lo
