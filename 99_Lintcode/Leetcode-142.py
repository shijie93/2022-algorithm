# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        # 使用快慢指针，刚开始都指向开头
        fast, slow = head, head

        # 开始移动指针
        while True:

            # 如果快指针走到头，则说明有环，返回
            if not (fast and fast.next): return

            # 按照快指针2，慢指针1的速度移动
            fast, slow = fast.next.next, slow.next

            # 此时快慢指针在某处相遇
            if fast == slow: break

        # 假设 a 为非环长度，b为环长度
        # fast_step = 2 * slow_step
        # fast_step = slow_step + n * b
        # slow_step = n * circle_len 代表目前停止的位置，慢指针共走了环程度的整数倍
        
        # 此时只需要让慢指针向前在移动a距离，那么慢指针必停在入口（k = a + m*b 一定在入口）
        # 所以只需要再取一个指针从开头移动，那么必定在入口相遇
        tmp = head
        while tmp != slow:
            tmp, slow = tmp.next, slow.next
        return tmp