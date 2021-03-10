class Solution:
    def minWindow(self, s: str, t: str) -> str:
        times = dict()
        for i, char in enumerate(t):
            if char in times:
                times[char] += 1
            else:
                times[char] = 1

        lo = 0
        ans = ""
        for hi in range(len(s)):
            if s[hi] in times:
                times[s[hi]] -= 1
            if max(times.values()) <= 0:
                while s[lo] not in times or times[s[lo]] < 0:
                    if s[lo] in times: times[s[lo]] += 1
                    lo += 1
                if len(ans) == 0 or len(ans) > hi - lo + 1:
                    ans = s[lo:hi + 1]
        return ans
