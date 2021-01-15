class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        ans = []
        for word in words:
            if len(word) > 0:
                ans.append(word)
        return ' '.join(ans[::-1])
