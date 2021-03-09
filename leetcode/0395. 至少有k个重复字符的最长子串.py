class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        d = dict()
        for char in s:
            if char not in d:
                d[char] = 1
            else:
                d[char] += 1
        
        # 
        for key, value in d.items():
            if value < k:
                return max([self.longestSubstring(str, k) for str in s.split(key)])
        return len(s)
