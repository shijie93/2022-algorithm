class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head: return head

        fast = slow = head

        while fast and slow:
            if fast.val != slow.val:
                slow = slow.next
                slow.val = fast.val
            
            fast = fast.next
        
        slow.next = None
        return head