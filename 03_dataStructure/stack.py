
class Stack:

    def __init__(self) -> None:
        self._stack = []

    def push(self, i):
        self._stack.append(i)

    def pop(self):
        if len(self._stack) > 0:
            return self._stack.pop()
        else:
            return None

    def __len__(self) -> int:
        return len(self._stack)

    def glance(self):
        if len(self._stack) > 0:
            return self._stack[-1]
        else:
            return None


if __name__ == '__main__':

    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.pop())
    print(s.glance())
    print(len(s))
