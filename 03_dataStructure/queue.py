class Queue:

    def __init__(self, size=32) -> None:
        self._queue = [0 for _ in range(size)]
        self.size = size
        self.front = 0
        self.rear = 0

    def is_empty(self):
        return self.front == self.rear
    
    def is_filled(self):
        return (self.rear + 1) % self.size == self.front

    
    def push(self, i):
        if not self.is_filled():
            self.rear = (self.rear + 1) % self.size
            self._queue[self.rear] = i
        else:
            raise IndexError("队列已满")
    
    def pop(self):
        if not self.is_empty():
            self.front = (self.front + 1) % self.size
        else:
            raise IndexError("空队列")

    def list(self):
        if self.rear > self.front:
            return self._queue[self.front+1:self.rear+1]
        else:
            return self._queue[self.front+1:] + self._queue[:self.rear+1]

if __name__ == '__main__':

    s = Queue(7)
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)
    s.push(6)
    s.pop()
    s.pop()
    s.pop()
    s.pop()
    s.pop()
    s.pop()
    s.push(4)
    s.push(5)
    s.push(6)

    print(s.list())

