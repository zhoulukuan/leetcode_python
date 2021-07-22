class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        nums = []
        index = 0
        while index < len(s):
            char = s[index]
            if ord('0') <= ord(char) <= ord('9'):
                start = index
                while ord('0') <= ord(s[index]) <= ord('9'): index += 1
                nums.append(int(s[start:index]))
            elif char == ']':
                last = len(stack) - 1
                while last >= 0 and stack[last] != '[':
                    last -= 1
                gen = ''.join(stack[last+1:]) * nums[-1]
                stack = stack[:last]
                nums.pop()
                stack.append(gen)
                index += 1
            else:
                stack.append(char)
                index += 1
        return ''.join(stack)
