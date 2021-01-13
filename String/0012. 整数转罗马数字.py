class Solution:
    def intToRoman(self, num: int) -> str:
        sign = [['I', 'IV', 'V', 'IX'],
                ['X', 'XL', 'L', 'XC'],
                ['C', 'CD', 'D', 'CM'],
                ['M']]
        ans = ""
        if num < 1 or num > 3999: return ans

        index = 0
        while num > 0:
            i = num % 10
            if i >= 1 and i <= 3:
                ans = sign[index][0] * i + ans
            elif i == 4:
                ans = sign[index][1] + ans
            elif i == 5:
                ans = sign[index][2] + ans
            elif i >= 6 and i <= 8:
                ans = sign[index][2] + sign[index][0] * (i - 5) + ans
            elif i == 9:
                ans = sign[index][3] + ans
            num //= 10
            index += 1
        return ans
