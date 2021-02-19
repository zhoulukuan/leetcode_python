class Solution:
    def myAtoi(self, s: str) -> int:
        max_num = 2**31 - 1
        min_num = -max_num - 1

        ans = 0
        sign = 1
        start = 0

        while start < len(s) and s[start] == ' ': start += 1
        if start < len(s) and s[start] == '-':
            sign = -1
            start += 1
        elif start < len(s) and s[start] == '+':
            start += 1

        for i in range(start, len(s)):
            if s[i] >= '0' and s[i] <= '9':
                ans = 10 * ans + int(s[i]) * sign
                if sign and ans >= max_num: return max_num
                if -sign and ans <= min_num: return min_num
            else:
                return ans
        return ans
