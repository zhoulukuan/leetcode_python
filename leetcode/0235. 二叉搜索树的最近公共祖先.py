class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while True:
            if root == p or root == q:
                return root
            f1 = self.search(root.left, p)
            f2 = self.search(root.left, q)
            if f1 and f2: root = root.left
            elif not f1 and not f2: root = root.right
            else: return root

    def search(self, root, node):
        val = node.val
        while root:
            if root.val == val: return True
            elif root.val > val: root = root.left
            else: root = root.right
        return False
