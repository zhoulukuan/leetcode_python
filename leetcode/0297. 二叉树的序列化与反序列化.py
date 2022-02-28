class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        def helper(root, ans):
            if not root:
                ans.append('X')
                return
            ans.append(str(root.val))
            helper(root.left, ans)
            helper(root.right, ans)
        ans = []
        helper(root, ans)
        return "_".join(ans)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        def helper(data):
            num = data.pop(0)
            if num == 'X':
                return None
            root = TreeNode(num)
            root.left = helper(data)
            root.right = helper(data)
            return root
        return helper(data.split("_"))
