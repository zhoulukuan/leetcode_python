class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # 双指针模板
        n = len(s)
        if n <= k + 1:
            return n

        lo, hi = 0, 0

        # 统计结果用的数组/字典等,可复用,不用每次重新初始化
        ans = k + 1
        c = [0 for _ in range(26)]
        offset = ord('A')

        # 右指针没到头
        while hi < n:
            c[ord(s[hi]) - offset] += 1
            # 左指针不满足条件则一直移动,且移动后不需要重置
            # 例如lo=1,hi=5;移动hi到6,lo可以直接从1开始判断,不用判断之前的位置
            # 因为0~6包括0~5这一子区间,而后者在迭代中证明了无法满足条件
            while max(c) + k < hi - lo + 1:
                c[ord(s[lo]) - offset] -= 1
                lo += 1
            ans = max(ans, hi - lo + 1)
            hi += 1
        return ans
