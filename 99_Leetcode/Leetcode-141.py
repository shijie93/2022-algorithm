# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        cur1 = cur2 = head
        while cur2 and cur2.next:
            cur1 = cur1.next
            cur2 = cur2.next.next

            if cur1 is cur2:
                return True

        return False