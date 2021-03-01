class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None: return head
        first = head
        second = head
        while second.next:
            second = second.next
            if second.next:
                second = second.next
                first = first.next
        
        n1 = head
        n2 = first.next
        first.next = None
        n1 = self.sortList(n1)
        n2 = self.sortList(n2)
        n3 = ListNode()
        ans = n3
        while n1 and n2:
            if n1.val <= n2.val:
                n3.next = n1
                n1 = n1.next
                n3 = n3.next
                n3.next = None
            else:
                n3.next = n2
                n2 = n2.next
                n3 = n3.next
                n3.next = None
        if n1:
            n3.next = n1
        if n2:
            n3.next = n2
        return ans.next
