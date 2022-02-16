# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:

        curA, curB = headA, headB
        while True:
            if (curA and curA is curB) or (not curA and not curB):
                return curA

            curA = curA.next if curA else headB
            curB = curB.next if curB else headA
        