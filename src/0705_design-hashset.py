class MyHashSet:
    def __init__(self):
        self.array = [False] * int(1e6 + 1)

    def add(self, key: int) -> None:
        self.array[key] = True

    def remove(self, key: int) -> None:
        self.array[key] = False

    def contains(self, key: int) -> bool:
        return self.array[key]
