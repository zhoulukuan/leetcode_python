class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.n = n
        ans = []
        if n == 0: return ans
        self.helper(ans, 0, 0, '')
        return ans
    
    # num1: 左括号数量  num0: 右括号数量
    def helper(self, ans, num0, num1, curr_string):
        if num1 == self.n:
            curr_string = curr_string + ')' * (num1 - num0)
            ans.append(curr_string)
            return
        
        self.helper(ans, num0, num1 + 1, curr_string + '(')
        if num1 > num0:
            self.helper(ans, num0 + 1, num1, curr_string + ')')
        return 
