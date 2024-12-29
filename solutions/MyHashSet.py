# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

class MyHashSet:

    def __init__(self):
        self.set = set()

    def add(self, key: int) -> None:
        self.set.add(hash(key))

    def remove(self, key: int) -> None:
        if hash(key) in self.set:
            self.set.remove(hash(key))

    def contains(self, key: int) -> bool:
        if hash(key) in self.set: return True
        return False

