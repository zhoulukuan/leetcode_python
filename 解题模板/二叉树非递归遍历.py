class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Visit:
    # 中序遍历
    def inOrder(self, root):
        seri = []
        stack = []
        # 当前节点或者栈内不为空则需要继续遍历
        while root or stack:
            while root:
                # 当前节点压入栈,并继续查找是否有左节点,直到最左面的节点也被压入栈
                # 此时root为None
                stack.append(root)
                # 节点入栈的时候可以直接打印
                seri.append(root.val)
                root = root.left
            # 弹出栈内节点
            node = stack.pop()
            # 若该节点不存在右节点,则root是None,会继续弹出下一个节点
            # 若存在右节点,则root被设置为右节点,程序转入右树去打印当前弹出节点的右树结果
            root = node.right
        return seri

    # 先序遍历
    def preOrder(self, root):
        seri = []
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            node = stack.pop()
            # 区分点: 不是在节点入栈的时候访问,因为节点可能存在左节点
            # 出栈的时候,因为根节点都在父节点前,可以直接打印
            seri.append(node.val)
            root = node.right
        return seri

    # 后序遍历
    def postOrder(self, root):
        seri = []
        stack = []
        # 后序遍历最大的不同: 需要一个节点帮助记录当前节点的右树有没有被访问过,如果访问过
        # 才可以直接打印否则要先访问右树
        last = None
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            # 注意不是弹出,因为可能存在node的右树没有访问,要先访问右树的情况
            node = stack[-1]
            # 右树为空或者访问过右树
            if not node.right or last == node.right:
                # 弹出当前节点,打印当前节点值
                stack.pop()
                seri.append(node.val)
                # root设置为空,继续弹出栈内节点
                root = None
                # last指向当前节点
                last = node
            # 右树没访问过,则转入右树
            # 或者右树为空,则root会设置为None,同样会继续弹出栈内节点
            else:
                root = node.right
                last = None
        return seri


if __name__ == '__main__':
    n3 = TreeNode(3)
    n5 = TreeNode(5)
    n6 = TreeNode(6)
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n4 = TreeNode(4)

    n5.left, n5.right = n3, n6
    n3.left, n3.right = n2, n4
    n2.left = n1
    v = Visit()
    print(v.inOrder(n5))
    print(v.preOrder(n5))
    print(v.postOrder(n5))
