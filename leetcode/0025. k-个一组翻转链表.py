class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        ans = ListNode()
        ans_head = ans
        stack = []
        while head:
            node, head = head, head.next
            node.next = None
            stack.append(node)
            if len(stack) == k:
                while len(stack) > 0:
                    last = stack.pop()
                    ans.next = last
                    ans = ans.next
        
        while len(stack) > 0:
            first = stack.pop(0)
            ans.next = first
            ans = ans.next
        return ans_head.next
