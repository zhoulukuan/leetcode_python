class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not len(nums): return None
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        if mid > 0:
            left = self.sortedArrayToBST(nums[0:mid])
            root.left = left
        if mid < len(nums) - 1:
            right = self.sortedArrayToBST(nums[mid+1:])
            root.right = right
        return root
