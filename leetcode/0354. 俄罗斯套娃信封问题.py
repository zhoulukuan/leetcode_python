class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x:x[0])
        n = len(envelopes)
        ans = 1
        dp = [1 for _ in range(n)]
        for i in range(1, n):
            for j in range(i):
                if envelopes[j][1] < envelopes[i][1] and envelopes[j][0] < envelopes[i][0]  and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
            if dp[i] > ans: ans = dp[i]
        return ans
