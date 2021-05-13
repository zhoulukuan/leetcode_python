import heapq
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        n = len(lists)
        count = 0
        heap = []
        for i in range(n):
            node = lists[i]
            if node:
                heapq.heappush(heap, (node.val, i, node))
                count += 1

        head = ListNode(0)
        curr = head
        while count > 0:
            _, i, node = heapq.heappop(heap)
            lists[i] = node.next
            curr.next = node
            node.next = None
            curr = curr.next
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))
            else:
                count -= 1
        return head.next
