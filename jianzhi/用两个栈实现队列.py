# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.s1 = []
        self.s2 = []
        
    def push(self, node):
        # write code here
        self.s1.append(node)
    
    def pop(self):
        # return xx
        if self.s1 == [] and self.s2 == []:
            return None
        elif self.s2 != []:
            return self.s2.pop()
        else:
            for i in range(len(self.s1)):
                self.s2.append(self.s1.pop())
            return self.s2.pop()