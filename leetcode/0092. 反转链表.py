class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        curr = ListNode(0)
        curr.next = head
        head = curr
        offset = right - left
        while left > 1 and curr.next:
            curr = curr.next
            left -= 1

        stack = []
        node = curr.next
        while offset >= 0:
            stack.append(node)
            node = node.next
            offset -= 1

        while len(stack) > 0:
            n = stack.pop()
            curr.next = n
            curr = curr.next
        curr.next = node
        return head.next
