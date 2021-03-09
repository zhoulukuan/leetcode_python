class Solution:
    # 法一:切分
        # 核心思想:如果某个字符在当前字符串中出现的次数少于k,那么最终结果一定是不包含该字符的,因此可以以该字符为切分字符,切分字符串
        # 对每个切分得到的字符串,恰好可以用相同的方法求子问题,因此是递归
    def longestSubstring(self, s: str, k: int) -> int:
        d = dict()
        for char in s:
            if char not in d:
                d[char] = 1
            else:
                d[char] += 1
        
        for key, value in d.items():
            if value < k:
                return max([self.longestSubstring(str, k) for str in s.split(key)])
        return len(s)

    # 法二:二分+双指针
    # 双指针和二分法本质一样,都需要数组具有相同的性质:区间t满足某个条件,区间扩大到t+1恰好不满足,因此本题不可以直接使用双指针法
    # 但是转化成字符数量后,就可以使用双指针了.对于区间t,右指针滑动必然增加或不变区间内字符数量,左指针滑动必然减少或者不变区间内的数量
    # 因此可以用包含多少种不同的字符作为双指针的条件
    def longestSubstring(self, s: str, k: int) -> int:
        ans = 0
        for num_char in range(1, 27):
            tot, sum, start = 0, 0, 0   # tot:总字符数量,sum:满足条件的字符数量
            d = dict()
            for end in range(0, len(s)):
                if s[end] in d:
                    d[s[end]] += 1
                else:
                    d[s[end]] = 1
                    tot += 1
                if d[s[end]] == k:
                    sum += 1
                while tot > num_char and start <= end:
                    d[s[start]] -= 1
                    if d[s[start]] == 0:
                        d.pop(s[start])
                        tot -= 1
                    elif d[s[start]] == k - 1:
                        sum -= 1
                    start += 1
                if sum == tot: ans = max(ans, end - start + 1)
        return ans
