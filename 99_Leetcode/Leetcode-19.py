class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        p1, self.next = self, head
        for i in range(n + 1):
            p1 = p1.next
        
        p2 = self
        while p1:
            p1 = p1.next
            p2 = p2.next

        p2.next = p2.next.next
        return self.next