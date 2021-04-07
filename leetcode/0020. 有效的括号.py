class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        left = ['(', '[', '{']
        right = [')', ']', '}']
        for char in s:
            if char in left:
                stack.append(char)
            else:
                if len(stack) == 0: return False
                top = stack.pop()
                if left.index(top) != right.index(char): return False
        return len(stack) == 0
