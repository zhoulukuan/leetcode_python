# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.pre = []
        self.tin = []

    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if len(pre) != len(tin):
            return None
        if len(pre) == 0:
            return None
        self.pre = pre
        self.tin = tin
        return self.helper(0, len(pre) - 1, 0, len(tin) - 1)

    def helper(self, pl, ph, tl, th):
        if pl > ph or tl > th:
            return None

        if pl == ph and tl == th:
            if self.pre[pl] == self.tin[tl]:
                return TreeNode(self.pre[pl])
            else:
                raise ValueError('Illegal input!')
        
        # Find how to split
        root = TreeNode(self.pre[pl])
        pos = tl - 1
        for i in range(tl,th+1):
            if self.pre[pl] == self.tin[i]:
                pos = i
        if pos == tl - 1:
            raise ValueError('Illegal input!')
        
        # Build subtree
        root.left = self.helper(pl + 1, pl + pos - tl, tl, pos - 1)
        root.right = self.helper(ph + pos + 1 - th, ph, pos + 1, th)
        return root