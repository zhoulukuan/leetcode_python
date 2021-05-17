class Solution:
    def fullJustify(self, words, maxWidth):
        ans = []
        index = 0
        n = len(words)

        res = maxWidth
        while index < n:
            start = index
            res -= len(words[start])
            while index + 1 < n and res >= len(words[index + 1]) + 1:
                index += 1
                res -= 1
                res -= len(words[index])

            ans.append(self.helper(words, start, index, maxWidth, res))
            index += 1
            res = maxWidth
        return ans


    def helper(self, words, start, end, maxWidth, res):
        n = end - start + 1
        if n == 1:
            res = words[start] + " " * res
        elif end == len(words) - 1:
            res = ""
            for i in range(start, end):
                res += words[i]
                res += " "
            res += words[end]
            res += " " * (maxWidth - len(res))
        else:
            num, over = res // (n - 1), res % (n - 1)
            res = ""
            for i in range(start, end):
                res += words[i]
                res += " " * (num + 1)
                if over > 0:
                    res += " "
                    over -= 1
            res += words[end]
        return res
