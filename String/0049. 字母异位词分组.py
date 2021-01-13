class Solution:
    def groupAnagrams(self, strs):
        p = self.prime()
        self.num = [next(p) for _ in range(26)]
        d = {}
        for string in strs:
            num = self.str2num(string)
            if num in d:
                d[num].append(string)
            else:
                d[num] = [string]
        ans = []
        for value in d.values():
            ans.append(value)
        return ans

    def str2num(self, s):
        # 哈希表映射
        ans = 1
        for i in s:
            ans *= self.num[ord(i) - ord('a')]
        return ans

    def prime(self):
        # 素数生成器,生成1000以内的素数
        def odd_iters():
            n = 1
            while n < 1000:
                n += 2
                yield n

        yield 2
        it = odd_iters()
        while True:
            n = next(it)
            yield n
            # lambda表达式无法访问外部变量,所以必须把n的值传进去
            it = filter(lambda x, n = n: x % n > 0, it)
