class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("capacity is not a non-negative int")

        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        if n + self.size > self._capacity:
            raise ValueError("the added cookies are greater than the capacity")

        self._size += n

    def withdraw(self, n):
        if n > self._size:
            raise ValueError("the withdrawed cookies is less than the size")

        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
