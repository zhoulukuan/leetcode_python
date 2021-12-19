from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        prime = self.genPrime()
        def strToNum(str):
            num = 1
            for char in str:
                num *= prime[ord(char) - ord('a')]
            return num

        d = defaultdict(list)
        for str in strs:
            num = strToNum(str)
            d[num].append(str)
        ans = []
        for key, values in d.items():
            ans.append(values)
        return ans

    def genPrime(self):
        nums = [i for i in range(2, 200)]
        ans = []
        index = 0
        while index < 26:
            num = nums[index]
            index += 1
            ans.append(num)
            nums = [i for i in nums if i % num > 0]
        return ans
