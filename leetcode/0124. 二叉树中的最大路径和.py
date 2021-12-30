class Solution:
    def __init__(self) -> None:
        self.ans = -1000

    def maxPathSum(self, root: TreeNode) -> int:
        self.helper(root)
        return self.ans

    def helper(self, root):
        if root is None: return 0
        left = self.helper(root.left)
        right = self.helper(root.right)

        maxV = root.val
        # 如果左树或者右树>0,累加进当前的根节点值中
        if left > 0:
            maxV += left
        if right > 0:
            maxV += right
        self.ans = max(self.ans, maxV)
        # 根节点如果<0,则不是必须选取的,可以舍弃
        return max(max(left, right) + root.val, 0)
