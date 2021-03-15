class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        len1 = self.getLen(headA)
        len2 = self.getLen(headB)
        if len1 >= len2:
            node1, node2 = headB, headA
        else:
            node1, node2 = headA, headB

        offset = abs(len1 - len2)
        while offset > 0:
            node2 = node2.next
            offset -= 1

        while node1:
            if node1 == node2:
                return node1
            else:
                node1, node2 = node1.next, node2.next
        return None

    def getLen(self, node):
        n = 0
        head = node
        while head:
            head = head.next
            n += 1
        return n
