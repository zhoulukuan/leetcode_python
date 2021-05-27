from collections import deque
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def dfs(root, parent):
            if not root: return
            root.par = parent
            dfs(root.left, root)
            dfs(root.right, root)
        dfs(root, None)

        queue = deque()
        queue.append(target)
        ans = []
        visited = set()
        visited.add(target.val)
        lvl = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                if k == lvl: 
                    ans.append(node.val)
                for next_node in (node.left, node.right, node.par):
                    if next_node and next_node.val not in visited:
                        queue.append(next_node)
                        visited.add(next_node.val)
            lvl += 1
        return ans  
