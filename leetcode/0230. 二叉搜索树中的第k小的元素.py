class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            node = stack.pop()
            k -= 1
            if k == 0: return node.val
            if node.right:
                root = node.right
        return -1
