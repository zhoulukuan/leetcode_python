class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 虚拟头部,规避只有一个节点的情况
        node = ListNode()
        node.next = head
        
        first = node
        for _ in range(n):
            if first.next is not None:
                first = first.next
            else:
                # 倒数数量超过链表长度
                return head
        
        second = node
        while first.next is not None:
            first = first.next
            second = second.next
        second.next = second.next.next
        return node.next
