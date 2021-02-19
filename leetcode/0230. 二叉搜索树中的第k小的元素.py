class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        ans = []
        while True:
            while root is not None:
                ans.append(root)
                root = root.left
            root = ans.pop()
            k -= 1
            if k == 0: 
                return root.val
            root = root.right
