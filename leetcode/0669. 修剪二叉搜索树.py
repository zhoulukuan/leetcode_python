class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        if root == None: return None
        curr = root.val
        if low <= curr <= high:
            left = self.trimBST(root.left, low, high)
            right = self.trimBST(root.right, low, high)
            root.left, root.right = left, right
            return root
        elif curr < low:
            return self.trimBST(root.right, low, high)
        else:
            return self.trimBST(root.left, low, high)
