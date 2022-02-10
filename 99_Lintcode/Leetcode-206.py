# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 递归方法
        # 将问题分解为 1->2->3->4<-5

        # 递归终止条件是当前为空，或者下一个节点为空
        if not head or not head.next:
            return head

        # 这里的cur就是最后一个节点
        cur = self.reverseList(head.next)

        # 如果链表是 1->2->3->4->5，那么此时的cur就是5
        # 而head是4，head的下一个是5，下下一个是空
        # 所以head.next.next 就是5->4
        head.next.next = head
        # 防止链表循环，需要将head.next设置为空
        head.next = None
        # 每层递归函数都返回cur，也就是最后一个节点
        return cur

        # # 迭代方法
        # # 由于需要翻转，此处需要定义两个指针，分别指向当前节点和上一个节点
        # cur, prev = head, None

        # # 循环更改指针的方向，直到当前节点为空，此时 prev 即为头结点
        # while cur:
        #     # cur.next = prev 即翻转
        #     # prev = cur 前节点指向当前
        #     # cur = cur.next 更新 cur
        #     cur.next, prev, cur = prev, cur, cur.next

        # # 返回翻转后的链表头结点
        # return prev