# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        cur = self
        up = 0
        while True:
            if not l1 and not l2: break

            a = l1.val if l1 else 0
            b = l2.val if l2 else 0

            cur.next = ListNode((a+b + up) % 10)
            up = (a+b + up) // 10

            if l1: l1 = l1.next
            if l2: l2 = l2.next
            cur = cur.next
        
        if up == 1:
            cur.next = ListNode(1)
        
        return self.next