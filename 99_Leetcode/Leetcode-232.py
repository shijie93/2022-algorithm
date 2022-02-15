class MyQueue:

    def __init__(self):
        self._stack1 = [] # 存放正序
        self._stack2 = [] # 存放倒序

    def push(self, x: int) -> None:
        # 如果 stack2 为空，则直接插入 stack1，否则将 stack2的元素放入stack1
        while len(self._stack2) > 0:
            self._stack1.append(self._stack2.pop())

        self._stack1.append(x)


    def pop(self) -> int:
        while len(self._stack1) > 0:
            self._stack2.append(self._stack1.pop())
        
        return self._stack2.pop()


    def peek(self) -> int:
        if len(self._stack2) > 0:
            return self._stack2[-1]
        else:
            return self._stack1[0]

    def empty(self) -> bool:
        return len(self._stack1) == 0 and len(self._stack2) == 0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()