class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        n = len(A)
        d = dict()

        ans = 0
        for i in range(n):
            for j in range(n):
                curr = A[i] + B[j]
                if curr in d:
                    d[curr] += 1
                else:
                    d[curr] = 1

        for i in range(n):
            for j in range(n):
                curr = C[i] + D[j]
                if -curr in d:
                    ans += d[-curr]
