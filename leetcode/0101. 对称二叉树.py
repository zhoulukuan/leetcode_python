class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return True
        return self.helper(root.left, root.right)

    def helper(self, left, right):
        if not left and not right: return True
        if left and not right: return False
        if not left and right: return False
        return left.val == right.val and self.helper(left.right, right.left) and self.helper(left.left, right.right)
