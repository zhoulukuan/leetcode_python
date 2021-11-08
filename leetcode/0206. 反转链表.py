class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        visual = ListNode(0)
        visual.next = head

        pre = visual
        curr = head
        while curr:
            next = curr.next
            curr.next = pre
            curr, pre = next, curr
        head.next = None
        return pre
