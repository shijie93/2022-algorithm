class MinStack:
    '''pop、top 和 getMin 操作总是在 非空栈 上调用。'''
    def __init__(self):
        self.cache = []
        self.minval = float('inf')

    def push(self, val: int) -> None:
        self.cache.append(val)
        if val < self.minval:
            self.minval = val

    def pop(self) -> None:
        ret = self.cache.pop()
        if len(self.cache) > 0:
            self.minval = min(self.cache)
        else:
            self.minval = float('inf')

    def top(self) -> int:
        return self.cache[-1]

    def getMin(self) -> int:
        return self.minval


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
