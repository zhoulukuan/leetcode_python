class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        small = ListNode()
        large = ListNode()
        n1 = small
        n2 = large

        while head is not None:
            if head.val < x:
                small.next = head
                small = small.next
            else:
                large.next = head
                large = large.next
            head = head.next
        # 要断开尾部的链接,否则会循环
        large.next = None
        small.next = n2.next
        return n1.next
