class Solution:
    def restoreIpAddresses(self, s: str):
        self.n = len(s)
        self.s = s + "######"
        ans = []
        ip = []
        self.helper(0, ip, ans)
        return ans

    def helper(self, start, ip, ans):
        num = len(ip)
        # 字符串用完则看是否刚好有4个数字
        if start == self.n and num == 4:
            ans.append('.'.join(ip))
            return
        # 越界终止
        if start > self.n or num > 4: return
        # 字符串没用完已经有4个数字或者字符串用完不到4个数字
        if start == self.n or num == 4: return

        # 字符串小于n且数字小于4个
        if (self.range(self.s[start], 0, 9)):
            self.helper(start + 1, ip + [self.s[start]], ans)
        if (self.range(self.s[start:start+2], 10, 99)):
            self.helper(start + 2, ip + [self.s[start:start+2]], ans)
        if (self.range(self.s[start:start+3], 100, 255)):
            self.helper(start + 3, ip + [self.s[start:start+3]], ans)

    def range(self, string, low, hi):
        if "#" in string: return False
        return int(string) >= low and int(string) <= hi
