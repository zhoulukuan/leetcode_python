from collections import defaultdict
class Solution:
    def countArrangement(self, n: int) -> int:
        nums = [i + 1 for i in range(n)]
        dive = defaultdict(list)
        for num in nums:
            for i in range(n):
                if num % (i + 1) == 0 or (i + 1) % num == 0:
                    dive[num].append(i)
        self.ans = 0

        def backtracking(path):
            if len(path) == n:
                self.ans += 1
                return
            for i in range(n):
                num = nums[i]
                if num != 0 and len(path) in dive[num]:
                    path.append(num)
                    nums[i] = 0
                    backtracking(path)
                    nums[i] = num
                    path.pop()
        backtracking([])
        return self.ans
