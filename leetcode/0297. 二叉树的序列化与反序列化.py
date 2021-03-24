class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        return self.seri_helper(root, 1001)

    def seri_helper(self, root, depth):
        if root == None: return []
        ans = [root.val]
        ans = ans + [-depth] + self.seri_helper(root.left, depth + 1)
        ans = ans + [-depth] + self.seri_helper(root.right, depth + 1)
        return ans

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        return self.dese_helper(data, 1001)

    def dese_helper(self, data, depth):
        if len(data) == 0: return None
        root = TreeNode(data[0])
        if len(data) == 1: return root

        index1 = data.index(-depth, 1)
        index2 = data.index(-depth, index1 + 1)
        left = self.dese_helper(data[index1 + 1:index2], depth + 1)
        right = self.dese_helper(data[index2 + 1:], depth + 1)
        root.left = left
        root.right = right
        return root
