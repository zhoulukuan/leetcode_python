from collections import defaultdict
class Solution:
    def canCross(self, stones) -> bool:
        n = len(stones)
        max_distance = stones[n - 1]

        dp = defaultdict(set)
        dp[0].add(1)
        for i in stones:
            steps = dp[i]
            for step in steps:
                next = i + step
                if next in stones:
                    if next == max_distance:
                        return True
                    for dstep in [-1, 0, 1]:
                        new_step = step + dstep
                        if new_step > 0 and new_step < n:
                            dp[next].add(new_step)
        return False
