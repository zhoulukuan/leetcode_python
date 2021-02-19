class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        fast = head
        slow = head
        while True:
            if not (fast and fast.next): return None
            fast = fast.next.next
            slow = slow.next
            if fast == slow: break
        fast = head
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return fast
