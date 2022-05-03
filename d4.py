class OrderedPair:
    def __init__(self, left = 0, right = 0):
        self.list = [int(left), int(right)]
        self.list.sort()

    def __str__(self):
        return f'({self.list[0]}, {self.list[1]})'

    def set_element(self, index, value):
        self.list[index] = value
        self.list.sort()

    def __add__(self, other):
        new = OrderedPair(self.list[0] + other.list[0], self.list[1] + other.list[1])
        return new

    def __sub__(self, other):
        new = OrderedPair(self.list[0] - other.list[0], self.list[1] - other.list[1])
        return new

    def __ge__(self, other):
        return sum(self.list) >= sum(other.list)

    def __eq__(self, other):
        return sum(self.list) == sum(other.list)
