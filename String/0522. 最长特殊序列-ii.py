class Solution:
    def findLUSlength(self, strs):
        # 核心思想: 最长特殊序列必定是某个字符串而不是某个字符串的子序列
        # 反证: 假如最长特殊序列是字符串a的子序列b而不是a,因为a可以通过删除字符变成b,所以b不是特殊序列,矛盾
        ans = ""
        for i in range(len(strs)):
            if len(strs[i]) <= len(ans):
                continue
            if self.helper(i, strs):
                ans = strs[i]
        return len(ans) if len(ans) > 0 else -1

    def helper(self, i, strs):
        s1 = strs[i]
        for j in range(len(strs)):
            s2 = strs[j]
            if j == i or len(s1) > len(s2): continue
            index = 0
            is_sub = True
            for c in s1:
                pos = s2.find(c, index)
                if pos == -1:
                    is_sub = False
                    break
                index = pos + 1
            if is_sub: return False
        return True
