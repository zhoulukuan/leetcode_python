class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for char in s:
            if not stack or stack[-1][0] != char:
                stack.append([char, 1])
            else:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
        
        ans = ""
        for char, times in stack:
            ans += char * times
        return ans
