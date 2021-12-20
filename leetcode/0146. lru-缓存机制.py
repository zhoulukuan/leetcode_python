class ListNode:
    def __init__(self, key=0, val=0, pre=None, next=None):
        self.key = key
        self.val = val
        self.pre = pre
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.curr = 0
        self.head = ListNode(-10000)
        self.tail = self.head
        self.hash = {}

    def get(self, key: int) -> int:
        if key not in self.hash:
            return -1
        node = self.hash[key]
        self.del_node(node)
        self.add_node_to_tail(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        node = ListNode(key, value)
        if key in self.hash:
            self.del_node(self.hash[key])
        self.add_node_to_tail(node)
        if self.curr > self.capacity:
            self.del_node(self.head.next)

    def del_node(self, delete):
        if delete == self.tail:
            pre = self.tail.pre
            pre.next = None
            self.tail = pre
        else:
            pre, next = delete.pre, delete.next
            pre.next, next.pre = next, pre
        self.curr -= 1
        self.hash.pop(delete.key)

    def add_node_to_tail(self, node):
        self.tail.next = node
        node.pre, node.next = self.tail, None
        self.tail = node
        self.curr += 1
        self.hash[node.key] = node
