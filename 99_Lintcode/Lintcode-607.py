class TwoSum:
    def __init__(self):
        self.buf = []
    """
    @param number: An integer
    @return: nothing
    """
    def add(self, number):
        # write your code here
        self.buf.append(number)

    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """
    def find(self, value):
        # write your code here
        d = set()
        for val in self.buf:
            if val not in d:
                d.add(value - val)
            else:
                return True
        return False


if __name__ == '__main__':
    s = TwoSum()
    s.add(1)
    s.add(3)
    s.add(5)
    print(s.find(4))
    print(s.find(7))
