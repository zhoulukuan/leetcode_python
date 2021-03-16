class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head:
            first = head.next
            if first:
                second = first.next
                while first and second:
                    first = first.next
                    if second: second = second.next
                    if second: second = second.next
                    if first == second: return True
        return False
