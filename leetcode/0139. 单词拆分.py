class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        word_set = set()
        length_set = set()
        memory = set()
        for word in wordDict:
            word_set.add(word)
            length_set.add(len(word))
        n = len(s)

        def backtracking(start):
            if start == n:
                return True
            if s[start:] in memory:
                return False
            for length in length_set:
                word = s[start:start+length]
                if word in word_set:
                    flag = backtracking(start+length)
                    if flag: return True
                    # 核心: memory,记忆失败的路径,防止超时
                    # 例如: 字符串aaaab, aaab失败后就可以不用再遍历
                    else: memory.add(s[start+length:])
            return False
        return backtracking(0)
