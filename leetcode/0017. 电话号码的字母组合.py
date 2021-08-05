class Solution:
    def __init__(self):
        self.num2char = {2:'abc', 3:'def', 4:'ghi', 5:'jkl', 6:'mno', 7:'pqrs', 8:'tuv', 9:'wxyz'}

    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        if len(digits) == 0: return ans

        def backtracking(path, i):
            if i == len(digits):
                ans.append(''.join(path))
                return
            for char in self.num2char[int(digits[i])]:
                path.append(char)
                backtracking(path, i + 1)
                path.pop()

        backtracking([], 0)
        return ans
