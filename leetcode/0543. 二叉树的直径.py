class Solution:
    def __init__(self):
        self.ans = 1

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.depth(root)
        return self.ans - 1

    def depth(self, root):
        if root == None: return 0
        l = self.depth(root.left)
        r = self.depth(root.right)
        self.ans = max(self.ans, l + r + 1)
        return max(l, r) + 1
