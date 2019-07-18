# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        h = len(array)
        if h == 0:
            return False
        w = len(array[0])
        if w == 0:
            return False
        
        i, j = 0, w - 1
        while (i <= w - 1 and j >= 0):
            if array[i][j] == target:
                return True
            elif array[i][j] < target:
                i += 1
            else:
                j -= 1
        return False