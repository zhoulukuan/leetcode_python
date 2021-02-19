class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = path.split("/")
        ans = []
        for p in paths:
            if p == '' or p == '.': 
                continue
            elif p == '..':
                if len(ans) > 0: ans.pop()
            else:
                ans.append(p)
        return '/' + '/'.join(ans)
