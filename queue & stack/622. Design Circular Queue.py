# Class to implement a circular queue with fixed capacity, supporting enqueue, dequeue, front, rear, and checks for emptiness or fullness.

class MyCircularQueue:
    
    def __init__(self, k: int):
        self.data = [0] * k
        self.capacity = k
        self.headIndex = 0
        self.count = 0
        

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.data[(self.headIndex + self.count) % self.capacity] = value
        self.count += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.headIndex = (self.headIndex + 1) % self.capacity
        self.count -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.data[self.headIndex]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.data[(self.headIndex + self.count -1) % self.capacity]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.capacity
