class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = dict()
        for num in nums1:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        
        ans = []
        for num in nums2:
            if num in d and d[num] > 0:
                ans.append(num)
                d[num] -= 1
        return ans
