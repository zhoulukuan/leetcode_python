class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.ans = -10000
        self.helper(root)
        return self.ans

    def helper(self, root):
        if root == None: return -10000
        leftMax = self.helper(root.left)
        rightMax = self.helper(root.right)
        data = [leftMax, rightMax, root.val, root.val + leftMax, root.val + rightMax, root.val + leftMax + rightMax, self.ans]
        self.ans = max(data)
        if leftMax < 0 and rightMax < 0:
            return root.val
        else:
            return root.val + max(leftMax, rightMax)
