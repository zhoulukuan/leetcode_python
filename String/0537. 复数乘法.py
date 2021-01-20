class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        num1 = self.convert(a)
        num2 = self.convert(b)
        real = num1[0] * num2[0] - num1[1] * num2[1]
        imag = num1[1] * num2[0] + num1[0] * num2[1]
        return str(real) + '+' + str(imag) + 'i'


    def convert(self, number):
        s = number.split('+')
        if len(s) != 2 or 'i' not in s[1]:
            return [0, 0]
        return [int(s[0]), int(s[1][:-1])]
