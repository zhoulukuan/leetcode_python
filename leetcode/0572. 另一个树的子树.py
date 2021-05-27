class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        if not root and not subRoot: return True
        if not root or not subRoot: return False
        if root.val == subRoot.val: 
            return self.helper(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def helper(self, root, subRoot):
        if not root and not subRoot: return True
        if not root or not subRoot: return False
        if root.val != subRoot.val: return False
        return self.helper(root.left, subRoot.left) and self.helper(root.right, subRoot.right)
