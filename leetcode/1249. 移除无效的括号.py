class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        left = 0
        right = 0
        pos = []
        rm = set()
        for i, char in enumerate(s):
            if char == '(':
                left += 1
                pos.append(i)
            elif char == ')':
                if right >= left:
                    # 右括号多于左括号直接删除
                    rm.add(i)
                else:
                    # 否则进行计数
                    right += 1
        # 左括号多于右括号,则删除多于的括号,遍历的时候pos已经记录了位置
        if left > right:
            for _ in range(left - right):
                rm.add(pos.pop())
        ans = ""
        for i in range(len(s)):
            if i not in rm:
                ans += s[i]
        return anss])
