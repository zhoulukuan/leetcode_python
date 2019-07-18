# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        front = 1
        back = 1
        for i in range(number):
            back = front + back
            front = back - front
        return front