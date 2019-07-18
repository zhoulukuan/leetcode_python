# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        o = ""
        for c in s:
            if c == ' ':
                o = o + '%20'
            else:
                o = o + c
        return o