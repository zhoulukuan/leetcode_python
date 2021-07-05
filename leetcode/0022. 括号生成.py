class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        self.dfs(0, 0, n, "", ans)
        return ans

    def dfs(self, nl, nr, n, path, ans):
        if nr > nl: return
        if nl == n: 
            ans.append(path + ")" * (n - nr))
            return
        else:
            self.dfs(nl + 1, nr, n, path + "(", ans)
            self.dfs(nl, nr + 1, n, path + ")", ans)
