class MyHashSet:

    def __init__(self):
        self.buckets = []
        for i in range(0,10000):
            self.buckets.append([])
        
    def add(self, key: int) -> None:
        hash = key % 10000
        if self.contains(key):
            return
        self.buckets[hash].append(key)
        
    def remove(self, key: int) -> None:
        hash = key % 10000
        for i in range(0, len(self.buckets[hash])):
            if self.buckets[hash][i] == key:
                self.buckets[hash].pop(i)
                return

    def contains(self, key: int) -> bool:
        hash = key % 10000
        for i in range(0, len(self.buckets[hash])):
            if self.buckets[hash][i] == key:
                return True
        return False   


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)