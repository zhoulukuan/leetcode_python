class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        node = head
        mid = head
        while node:
            node = node.next
            if node: 
                node = node.next
                mid = mid.next
        return mid
