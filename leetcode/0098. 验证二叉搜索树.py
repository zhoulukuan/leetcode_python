class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if root == None: return True
        self.flag = True
        def getMinMax(root):
            if root == None or not self.flag: return None, None
            leftMin, leftMax = getMinMax(root.left)
            rightMin, rightMax = getMinMax(root.right)
            if leftMax and leftMax >= root.val: self.flag = False
            if rightMin and rightMin <= root.val: self.flag = False
            minV = leftMin if leftMin else root.val
            maxV = rightMax if rightMax else root.val
            return minV, maxV
        getMinMax(root)
        return self.flag
