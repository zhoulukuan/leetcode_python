class Solution:
    def isPalindrome(self, s: str) -> bool:
        lo, hi = 0, len(s) - 1
        s = s.lower()
        while lo <= hi:
            while lo < hi and not('a' <= s[lo] <= 'z'
            or '0' <= s[lo] <= '9'):
                lo += 1
            while lo < hi and not('a' <= s[hi] <= 'z' 
            or '0' <= s[hi] <= '9'):
                hi -= 1
            if s[lo] != s[hi]: return False
            else:
                lo += 1
                hi -= 1
        return True
