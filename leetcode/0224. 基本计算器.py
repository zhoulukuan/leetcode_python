class Solution:
    def calculate(self, s: str) -> int:
        nums = []
        ops = []
        s = s.replace(" ", "").replace("(-", "(0-").replace("(+", "(")
        if s[0] == "-":
            s = '0' + s
        i = 0
        while i < len(s):
            char = s[i]
            if self.isDigit(char):
                num = ord(char) - ord('0')
                i += 1
                while i < len(s) and self.isDigit(s[i]):
                    num = num * 10 + ord(s[i]) - ord('0')
                    i += 1
                nums.append(num)
            elif char == ')':
                if ops[-1] == '(':
                    ops.pop()
                else:
                    self.cal(nums, ops)
                    ops.pop()
                i += 1
            elif char == '(':
                ops.append(char)
                i += 1
            else:
                self.cal(nums, ops)
                ops.append(char)
                i += 1
        self.cal(nums, ops)
        return nums[0]

    def cal(self, nums, ops):
        while len(nums) >= 2 and len(ops) > 0 and ops[-1] != '(':
            n1 = nums.pop()
            n2 = nums.pop()
            op = ops.pop()
            n = n1 + n2 if op == '+' else n2 - n1
            nums.append(n)

    def isDigit(self, char):
        return char >= '0' and char <= '9'
