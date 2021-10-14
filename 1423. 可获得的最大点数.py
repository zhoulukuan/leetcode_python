class Solution:
    def maxScore(self, cardPoints, k: int) -> int:
        n = len(cardPoints)
        if n <= k: return sum(cardPoints)

        total = 0
        ans = float('inf')
        windows = 0
        curr = 0
        k = n - k
        for i in range(n):
            total += cardPoints[i]
            curr += cardPoints[i]
            windows += 1
            if windows > k:
                curr -= cardPoints[i - k]
                windows -= 1
            if windows == k:
                ans = min(ans, curr)
        return total - ans
