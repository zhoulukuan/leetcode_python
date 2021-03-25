from collections import defaultdict
class Solution:
    def verticalTraversal(self, root: TreeNode):
        d = defaultdict(list)
        self.generate(d, root, 0, 0)
        ans = []
        tmp = -10000
        curr = []
        for i, j in sorted(d.keys()):
            if i != tmp:
                if len(curr) > 0:
                    ans.append(curr)
                    curr = []
            curr.extend(sorted(d[i, j]))
            tmp = i
        if len(curr) > 0: ans.append(curr)
        return ans

    def generate(self, d, root, col, row):
        if root == None: return
        d[(col, row)].append(root.val)
        self.generate(d, root.right, col + 1, row + 1)
        self.generate(d, root.left, col - 1, row + 1)
