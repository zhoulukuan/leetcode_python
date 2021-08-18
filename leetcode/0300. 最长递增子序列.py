class Solution:
    def lengthOfLIS(self, nums) -> int:
        d = []
        for num in nums:
            if not d or num > d[-1]:
                d.append(num)
            else:
                lo = 0
                hi = len(d)
                while lo < hi:
                    mid = (lo + hi) // 2
                    midV = d[mid]
                    if midV < num:
                        lo = mid + 1
                    else:
                        hi = mid
                d[lo] = num
        return len(d)
