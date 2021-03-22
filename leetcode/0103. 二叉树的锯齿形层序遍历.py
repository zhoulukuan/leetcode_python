class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None: return []

        ans = []
        data1 = [root]
        num1 = 1
        data2 = []
        num2 = 0

        while True:
            if num1 > 0:
                curr_ans = []
                while num1 > 0:
                    node = data1.pop(0)
                    num1 -= 1
                    if (node.left):
                        data2.append(node.left)
                        num2 += 1
                    if (node.right):
                        data2.append(node.right)
                        num2 += 1
                    curr_ans.append(node.val)
                ans.append(curr_ans)
            
            if num2 > 0:
                curr_ans = []
                while num2 > 0:
                    node = data2.pop(0)
                    num2 -= 1
                    if (node.left):
                        data1.append(node.left)
                        num1 += 1
                    if (node.right):
                        data1.append(node.right)
                        num1 += 1
                    curr_ans.append(node.val)
                ans.append(curr_ans[::-1])

            if num1 == 0 and num2 == 0:
                break
        return ans
