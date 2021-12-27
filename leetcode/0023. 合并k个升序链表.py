import heapq
from typing import List
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        def __lt__(a: ListNode, b: ListNode):
            return a.val < b.val
        ListNode.__lt__ = __lt__

        candidate = []
        for node in lists:
            heapq.heappush(candidate, (node.val, node))

        curr = ListNode(0)
        head = curr
        while len(candidate) > 0:
            val, node = heapq.heappop(candidate)
            if node.next:
                heapq.heappush(candidate, (node.next.val, node.next))
            curr.next = node
            curr = curr.next
        return head.next
