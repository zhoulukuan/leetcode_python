from collections import deque
class Solution:
    def cloneGraph(self, node):
        if node == None: return None
        queue = deque([node])
        used_set = set()
        used_set.add(node.val)

        copy_node = Node(node.val)
        copy_node_set = dict()
        copy_node_set[node.val] = copy_node
        while len(queue) > 0:
            node = queue.popleft()
            used_set.add(node.val)
            self.add(node, queue, used_set, copy_node_set)
        return copy_node


    def add(self, node, queue, used_set, copy_node_set):
        v = node.val
        if v not in copy_node_set:
            copy_node = Node(v)
            copy_node_set[v] = copy_node
        else:
            copy_node = copy_node_set[v]

        for neighbor in node.neighbors:
            connect_val = neighbor.val
            if connect_val not in used_set:
                used_set.add(connect_val)
                queue.append(neighbor)
            if connect_val not in copy_node_set:
                neighbor_copy_node = Node(connect_val)
                copy_node_set[connect_val] = neighbor_copy_node
            else:
                neighbor_copy_node = copy_node_set[connect_val]
            copy_node.neighbors.append(neighbor_copy_node)
