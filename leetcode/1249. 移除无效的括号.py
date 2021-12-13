class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        left = 0
        right = 0
        pos = []
        rm = set()
        for i, char in enumerate(s):
            if char == '(':
                left += 1
                pos.append(i)
            elif char == ')':
                if right >= left:
                    rm.add(i)
                else:
                    right += 1
        if left > right:
            for _ in range(left - right):
                rm.add(pos.pop())
        ans = ""
        for i in range(len(s)):
            if i not in rm:
                ans += s[i]
        return anss])
