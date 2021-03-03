class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()

        for index, num in enumerate(nums):
            another = target - num
            if another in d:
                return [d[another], index]
            else:
                d[num] = index
        return [-1, -1]
