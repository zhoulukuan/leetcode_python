import copy
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i + 1 for i in range(n)]
        ans = []

        def backtracking(path, start):
            if len(path) == k:
                ans.append(path.copy())
            for i in range(start, n):
                num = nums[i]
                if num != 0:
                    nums[i] = 0
                    path.append(num)
                    backtracking(path, i)
                    path.pop()
                    nums[i] = num
        backtracking([], 0)
        return ans
