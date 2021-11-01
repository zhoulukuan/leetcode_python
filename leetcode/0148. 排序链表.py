class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        # 切分
        first = head
        second = head.next
        while second is not None:
            second = second.next
            if second: 
                second = second.next
                first = first.next
        half1 = head
        half2 = first.next
        first.next = None

        # merge
        half1 = self.sortList(half1)
        half2 = self.sortList(half2)
        visual = ListNode(0)
        node = visual
        while half1 and half2:
            val1 = half1.val
            val2 = half2.val
            if val1 <= val2:
                node.next = half1
                half1 = half1.next
            else:
                node.next = half2
                half2 = half2.next
            node = node.next
        if half1:
            node.next = half1
        if half2:
            node.next = half2
        return visual.next
