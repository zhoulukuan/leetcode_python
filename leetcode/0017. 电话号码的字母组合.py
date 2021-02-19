class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.digits = digits
        self.num2char = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }
        ans = []
        if len(self.digits) == 0: return ans
        self.helper(ans, "", 0)
        return ans

    def helper(self, ans, s, i):
        if len(s) == len(self.digits):
            ans.append(s)
            return
        for char in self.num2char[self.digits[i]]:
            self.helper(ans, s + char, i + 1)
