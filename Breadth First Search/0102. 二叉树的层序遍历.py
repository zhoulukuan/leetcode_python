class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None: return []

        curr_num = 1
        data = [root]
        ans = []
        while len(data) > 0:
            next_num = 0
            curr = []
            while curr_num > 0:
                node = data.pop(0)
                curr.append(node.val)
                if node.left:
                    data.append(node.left)
                    next_num += 1
                if node.right:
                    data.append(node.right)
                    next_num += 1
                curr_num -= 1
            ans.append(curr)
            curr_num = next_num
        return ans
