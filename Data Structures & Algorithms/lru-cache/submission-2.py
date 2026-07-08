class LRUCache:

    def __init__(self, capacity: int):
        self.lookup =  dict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.lookup:
            return -1
        num = self.lookup.pop(key)
        self.lookup[key] = num
        return num

    def put(self, key: int, value: int) -> None:
        if key in self.lookup:
            self.lookup.pop(key)
            self.lookup[key] = value
            return
        if len(self.lookup) == self.capacity:
            first = next(iter(self.lookup))
            self.lookup.pop(first)
            self.lookup[key] = value
        else:
            self.lookup[key] = value
        return

