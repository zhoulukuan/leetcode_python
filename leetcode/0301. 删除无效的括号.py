class Solution:
    def removeInvalidParentheses(self, s: str):
        ans = set()
        self.max = 0
        self.dfs("", 0, 0, s, 0, ans)
        return list(ans)

    def dfs(self, path, left, right, s, i, ans):
        if right > left or left - right > len(s) - i or len(path) + len(s) - i < self.max:
            return
        if i == len(s) and left == right:
            if len(path) > self.max:
                self.max = len(path)
                ans.clear()
                ans.add(path)
            elif len(path) == self.max:
                ans.add(path)
            return
        char = s[i]
        if char == '(':
            self.dfs(path + char, left + 1, right, s, i + 1, ans)
        elif char == ')':
            self.dfs(path + char, left, right + 1, s, i + 1, ans)
        else:
            self.dfs(path + char, left, right, s, i + 1, ans)

        if char == '(' or char == ')':
            self.dfs(path, left, right, s, i + 1, ans)
