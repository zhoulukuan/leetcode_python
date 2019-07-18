# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        # write code here
        if number <= 3:
            return number
        front = 1
        back = 1
        for i in range(number):
            back = front + back
            front = back - front
        return front