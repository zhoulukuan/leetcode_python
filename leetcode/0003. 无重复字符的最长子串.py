class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 双指针
        # start_pos记录指针开始位置
        start_pos = -1
        max_len = 0
        d = {}
        for i in range(len(s)):
            if s[i] in d:
                # 假如元素出现过,更新指针开始位置,满足条件:
                # 开始位置必须>=该元素上一次出现的位置
                # 开始位置必须>=上一次的开始位置,比如abba这种字符串,在i=2位置更新了start_pos到第二个b之后,
                # a=0仍然保留在字典中,如果不加这个限制条件就会用第二个a减去第一个a的位置作为max_len
                start_pos = max(d[s[i]], start_pos)
            # 更新元素位置和最大长度
            d[s[i]] = i
            max_len = max(max_len, i - start_pos)
        return max_len
    
from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        low, fast = 0, 0
        times = defaultdict(int)
        diffNum, totalNum = 0, 0
        ans = 0
        while fast < n:
            char = s[fast]
            times[char] += 1
            totalNum += 1
            if times[char] == 1:
                diffNum += 1
            while totalNum > diffNum:
                char = s[low]
                low += 1
                times[char] -= 1
                totalNum -= 1
                if times[char] == 0:
                    diffNum -= 1
            ans = max(ans, fast - low + 1)
            fast += 1
        return ans
