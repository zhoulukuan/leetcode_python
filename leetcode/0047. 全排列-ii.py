class Solution:
    def permuteUnique(self, nums):
        n = len(nums)
        num_dict = {}
        for num in nums:
            if num not in num_dict:
                num_dict[num] = 1
            else:
                num_dict[num] += 1

        ans = set()
        def backtracking(path):
            if len(path) == n:
                ans.add(tuple(path.copy()))
            keys = list(num_dict.keys())
            for num in keys:
                num_dict[num] -= 1
                if num_dict[num] == 0:
                    num_dict.pop(num)
                path.append(num)
                backtracking(path)
                path.pop()
                if num not in num_dict:
                    num_dict[num] = 1
                else:
                    num_dict[num] += 1
        backtracking([])
        return list(ans)
