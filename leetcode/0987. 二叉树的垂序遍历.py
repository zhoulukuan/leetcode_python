from collections import defaultdict
class Solution:
    def verticalTraversal(self, root: TreeNode):
        pos = defaultdict(list)
        self.generate(pos, root, 0, 0)
        ans = []
        curr_col = []
        for (col, row), vals in sorted(pos.items()):
            if len(curr_col) == 0:
                curr_col = [col]
            elif col != curr_col[0]:
                ans.append(curr_col[1:])
                curr_col = [col]
            curr_col.extend(sorted(vals))
        if len(curr_col):
            ans.append(curr_col[1:])
        return ans

    def generate(self, pos, root, row, col):
        if not root: return
        pos[(col, row)].append(root.val)
        self.generate(pos, root.left, row + 1, col - 1)
        self.generate(pos, root.right, row + 1, col + 1)
