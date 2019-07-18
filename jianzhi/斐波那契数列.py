# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        front = 0
        back = 1
        for i in range(n):
            back = front + back
            front = back - front
        return front