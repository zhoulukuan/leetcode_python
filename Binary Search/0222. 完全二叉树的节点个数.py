class Solution:
    def countNodes(self, root):
        if root is None: return 0
        # 计算树的深度
        depth = 0
        node = root
        while node.left is not None:
            node = node.left
            depth += 1

        node = root
        ans = 2 ** (depth + 1) - 1
        for k in range(0, depth + 1):
            rh = self.getHeight(node.right)
            # 若右树深度和总深度一致,左树已经被填满,到右树继续找分界点
            if rh + k == depth:
                node = node.right
            else:
            # 若右树深度小于总深度,右树最底层是空的,到左树找分界点
                node = node.left
                ans -= 2 ** (depth - k - 1)
        return ans

    def getHeight(self, root):
        k = 0
        while root is not None:
            k += 1
            root = root.left
        return k
