class Solution:
    def evalRPN(self, tokens) -> int:
        sign = ["+", "-", "*", "/"]
        stack = []
        for token in tokens:
            if token not in sign:
                stack.append(token)
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                num = self.helper(num1, num2, token)
                stack.append(num)
        return int(stack[0])

    def helper(self, num1, num2, token):
        num1, num2 = int(num1), int(num2)
        if token == "+":
            return num1 + num2
        elif token == "-":
            return num1 - num2
        elif token == "*":
            return num1 * num2
        else:
            return num1 // num2 if num1 * num2 >= 0 else -(abs(num1) // abs(num2))
