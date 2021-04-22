class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        pos = []
        for i in range(len(s)):
            char = s[i]
            if char == '(':
                stack.append(char)
                pos.append(i)
            elif char == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                    pos.pop()
                else:
                    stack.append(char)
                    pos.append(i)

        pos = set(pos)
        return "".join([s[i] for i in range(len(s)) if i not in pos])
