class LRUCache:

    def __init__(self, capacity: int):
        self.hashmap = dict()
        self.capacity = capacity
        self.num = 0

        self.head = ListNode(0)
        self.tail = ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1
        node = self.hashmap[key]

        self.del_node(node)
        self.add_node_tail(node)
        return node.val


    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            node = self.hashmap[key]
            node.val = value
            self.del_node(node)
            self.add_node_tail(node)
        else:
            if self.num >= self.capacity:
                self.hashmap.pop(self.head.next.key)
                self.del_node(self.head.next)
                self.num -= 1
            node = ListNode(key, value)
            self.add_node_tail(node)
            self.hashmap[key] = node
            self.num += 1

    def del_node(self, node):
        prev = node.prev
        next = node.next
        prev.next, next.prev = next, prev

    def add_node_tail(self, node):
        last = self.tail.prev
        last.next, node.next = node, self.tail
        node.prev, self.tail.prev = last, node
