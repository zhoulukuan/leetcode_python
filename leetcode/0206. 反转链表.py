class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        curr_node = head
        if head:
            next_node = curr_node.next
        else:
            return head

        while next_node:
            next_next_node = next_node.next
            next_node.next = curr_node
            curr_node, next_node = next_node, next_next_node
        head.next = None
        return curr_node
