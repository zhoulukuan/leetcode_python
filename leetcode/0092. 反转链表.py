class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if left == right or not head or not head.next: return head

        visual = ListNode(0, head)
        start = visual
        for _ in range(left - 1):
            start = start.next
        curr = start.next

        nodes = []
        for _ in range(right - left + 1):
            nodes.append(curr)
            curr = curr.next
        end = curr

        node = start
        for _ in range(len(nodes)):
            node.next = nodes.pop()
            node = node.next
        node.next = end
        return visual.next
