class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        l = len(strs)
        num0 = [0 for _ in range(l)]
        num1 = [0 for _ in range(l)]
        for i, s in enumerate(strs):
            a, b = 0, 0
            for c in s:
                if c == '0': a += 1
                if c == '1': b += 1
            num0[i] = a
            num1[i] = b
        
        # 01背包,容量维度是+1的,因为要计算0容量的基础态;但是物体是不需要额外增加维度的
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(l):
            for c1 in range(m, -1, -1):
                for c2 in range(n, -1, -1):
                    if c1 >= num0[i] and c2 >= num1[i]:
                        dp[c1][c2] = max(dp[c1][c2], dp[c1 - num0[i]][c2 - num1[i]] + 1)
        return dp[m][n]
