class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root == None: return None
        currVal = root.val
        if currVal < val:
            return self.searchBST(root.right, val)
        elif currVal > val:
            return self.searchBST(root.left, val)
        else:
            return root
