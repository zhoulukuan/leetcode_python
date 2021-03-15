class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        n1 = ListNode(1)
        n2 = ListNode(2)
        head1, head2 = n1, n2
        while head:
            n1.next = head
            n1, head = n1.next, head.next
            n1.next = None

            if head:
                n2.next = head
                n2, head = n2.next, head.next
                n2.next = None
        head1, head2 = head1.next, head2.next
        n1.next = head2
        return head1
