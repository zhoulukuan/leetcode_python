class Solution:
    def compress(self, chars):
        ans = 0
        start = 0
        while start < len(chars):
            end = start + 1
            while end < len(chars) and chars[end] == chars[start]: end += 1
            
            chars[ans] = chars[start]
            ans += 1
            if end - start > 1:
                num = str(end - start)
                for t in num:
                    chars[ans] = t
                    ans += 1
            start = end
        return ans
