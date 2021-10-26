import random
class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.n = len(self.w)
        self.sum = self.w[0]
        for i in range(1, self.n):
            self.sum += self.w[i]
            self.w[i] += self.w[i - 1]

    def pickIndex(self) -> int:
        num = random.random() * self.sum
        lo, hi = 0, self.n
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if self.w[mid] <= num:
                lo = mid + 1
            else:
                hi = mid
        return lo

