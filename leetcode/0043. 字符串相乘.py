class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1 = len(num1)
        n2 = len(num2)
        num1 = num1[::-1]
        num2 = num2[::-1]
        temp = [0 for _ in range(n1 + n2 + 1)]
        for i in range(n1):
            for j in range(n2):
                temp[i + j] += int(num1[i]) * int(num2[j])

        for i in range(n1 + n2):
            if temp[i] >= 10:
                temp[i + 1] += temp[i] // 10
                temp[i] = temp[i] % 10
        end = n1 + n2
        while (end >= 1 and temp[end] == 0): end -= 1
        ans = ''
        for i in range(0, end + 1):
            ans = str(temp[i]) + ans
        return ans
