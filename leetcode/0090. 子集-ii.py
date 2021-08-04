class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n == 0: return None

        nums.sort()
        ans = set()
        def dfs(i, path):
            if i == n:
                ans.add(tuple(path))
                return
                
            dfs(i + 1, path)

            path.append(nums[i])
            dfs(i + 1, path)
            path.pop()

        dfs(0, [])
        return list(ans)
