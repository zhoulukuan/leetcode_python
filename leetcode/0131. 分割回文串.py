import copy
class Solution:
    def partition(self, s: str):
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = True

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    if i + 1 == j: dp[i][j] = True
                    else: dp[i][j] = dp[i + 1][j - 1]

        ans = []
        def backtracking(start, path):
            if start == n:
                ans.append(path.copy())
            for end in range(start, n):
                if not dp[start][end]:
                    continue
                path.append(s[start:end+1])
                backtracking(end+1, path)
                path.pop()
            return
        backtracking(0, [])
        return ans
