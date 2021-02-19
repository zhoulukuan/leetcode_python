class Solution:
    def __init__(self):
        super().__init__()
        self.max_num = 2**31

    def nextGreaterElement(self, n: int) -> int:
        chars = list(str(n))
        i = len(chars) - 1
        while i >= 1 and chars[i] <= chars[i - 1]: i -= 1
        if i >= 1:
            index = self.binarySearch(chars[i:][::-1], chars[i - 1]) + i
            chars[i - 1], chars[index] = chars[index], chars[i - 1]
            chars[i:] = chars[i:][::-1]
            ans = ''.join(chars)
            return int(ans) if int(ans) < self.max_num else -1
        return -1

    def binarySearch(self, data, target):
        lo, hi = 0, len(data)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if data[mid] <= target:
                lo = mid + 1
            else:
                hi = mid
        return len(data) - 1 - lo
