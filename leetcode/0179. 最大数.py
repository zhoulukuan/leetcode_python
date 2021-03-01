from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums) -> str:
        def compare(s1, s2):
            n1 = int(s1 + s2)
            n2 = int(s2 + s1)
            return n2 - n1  # 返回结果是正数则交换两元素,不能返回逻辑True/False
        ans = [str(n) for n in nums]
        ans.sort(key=cmp_to_key(compare))
        return ''.join(ans).lstrip('0') or '0'
