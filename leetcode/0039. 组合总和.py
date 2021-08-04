class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []

        def backtracking(target, path, start):
            if target == 0:
                ans.append(path.copy())
                return
            for i in range(start, len(candidates)):
                num = candidates[i]
                if target >= num:
                    target -= num
                    path.append(num)
                    backtracking(target, path, i)
                    path.pop()
                    target += num
                else:
                    break
            
        backtracking(target, [], 0)
        return ans
