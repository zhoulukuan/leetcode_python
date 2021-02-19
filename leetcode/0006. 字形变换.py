class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if (numRows == 1): return s
        if (numRows == 2): return s[0::2] + s[1::2]
        l = 2 * numRows - 2
        t = len(s) // l + 1
        ans = ""
        for i in range(numRows):
            for j in range(t):
                ans += s[i + j * l] if i + j * l < len(s) else ""
                if i != 0 and i != numRows - 1:
                    ans += s[(j + 1) * l - i] if (j + 1) * l - i < len(s) else ""
        return ans
