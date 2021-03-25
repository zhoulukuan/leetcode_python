class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root == None: return [-1001]
        ans = [root.val]
        ans = ans + self.serialize(root.left)
        ans = ans + self.serialize(root.right)
        return ans


    def deserialize(self, data):
        val = data.pop(0)
        if val == -1001: return None
        root = TreeNode(val)
        root.left = self.deserialize(data)
        root.right = self.deserialize(data)
        return root
