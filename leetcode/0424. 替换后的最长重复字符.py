from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        low, fast = 0, 0
        n = len(s)

        ans = 0
        times = defaultdict(int)
        totalNum = 0
        maxNum = 0
        while fast < n:
            char = s[fast]
            times[char] += 1
            totalNum += 1
            if times[char] > maxNum:
                maxNum = times[char]
            while totalNum - maxNum > k:
                char = s[low]
                low += 1
                times[char] -= 1
                totalNum -= 1
                if times[char] == maxNum - 1:
                    maxNum = max(times.values())
            ans = max(ans, fast - low + 1)
            fast += 1
        return ans
