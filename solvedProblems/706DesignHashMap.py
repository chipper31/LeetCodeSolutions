class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val

class MyHashMap:
    def __init__(self):
        self.buckets = []
        for i in range(0,10000):
            self.buckets.append([])
        
    def put(self, key: int, value: int) -> None:
        hash = key % 10000
        for i in range(0,len(self.buckets[hash])):
            if self.buckets[hash][i].key == key:
                self.buckets[hash][i].val = value
                return
        self.buckets[hash].append(Node(key, value))

    def get(self, key: int) -> int:
        hash = key % 10000
        for i in range(0,len(self.buckets[hash])):
            if self.buckets[hash][i].key == key:
                return self.buckets[hash][i].val

        return -1

    def remove(self, key: int) -> None:
        hash = key % 10000
        for i in range(0,len(self.buckets[hash])):
            if self.buckets[hash][i].key == key:
                self.buckets[hash].pop(i)
                return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)