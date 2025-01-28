#Class to calculate the moving average of all the integears in the sliding window.

class MovingAverage:

    def __init__(self, size: int):
        self.queue = []
        self.size = size

    def next(self, val: int) -> float:
        size, queue = self.size, self.queue
        queue.append(val)
        window_sum = sum(queue[-size:])
        return window_sum / min(len(queue), size)