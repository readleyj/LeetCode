class CustomStack:

    def __init__(self, maxSize: int):
        self.max_size = maxSize
        self.array = []

    def push(self, x: int) -> None:
        if len(self.array) != self.max_size:
            self.array.append(x)

    def pop(self) -> int:
        if self.array:
            return self.array.pop()

        return -1

    def increment(self, k: int, val: int) -> None:
        for idx in range(min(len(self.array), k)):
            self.array[idx] += val
