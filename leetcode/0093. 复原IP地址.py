class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        s = s + "#####"
        ans = []
        self.dfs(0, n, s, [], ans)
        return ans

    def dfs(self, i, n, s, path, ans):
        resNum = 4 - len(path)
        # 满足条件
        if i == n and resNum == 0: 
            ans.append(".".join(path))
            return
        # 剪枝
        if i >= n or resNum * 3 < n - i or resNum > n - i:
            return

        num = s[i:i+1]
        if self.valid(num):
            self.dfs(i+1, n, s, path + [num], ans)
        num = s[i:i+2]
        if self.valid(num):
            self.dfs(i+2, n, s, path + [num], ans)
        num = s[i:i+3]
        if self.valid(num):
            self.dfs(i+3, n, s, path + [num], ans)

    def valid(self, num):
        if "#" in num or (num[0] == '0' and num != "0"): return False
        return int(num) <= 255
