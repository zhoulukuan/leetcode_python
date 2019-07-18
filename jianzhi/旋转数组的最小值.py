# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        n = len(rotateArray)
        if n == 0:
            return 0
        if n == 1:
            return rotateArray[0]
        if rotateArray[0] < rotateArray[n - 1]:
            return rotateArray[0]

        lo = 0
        hi = n - 1
        while (lo < hi - 1):
            if rotateArray[lo] < rotateArray[hi]:
                return rotateArray[lo]
            mid = (lo + hi) / 2
            if rotateArray[mid] > rotateArray[lo]:
                lo = mid
            elif rotateArray[mid] < rotateArray[hi]:
                hi = mid
            else:
                if rotateArray[hi] == rotateArray[mid]:
                    hi -= 1
                else:
                    lo += 1
        return min(rotateArray[hi], rotateArray[lo])