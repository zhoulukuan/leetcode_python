class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root == None: return
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left, root.right = root.right, root.left
        return root
