class MyHashMap:

    def __init__(self):
        self.keys = list()
        self.values = list()

    def put(self, key: int, value: int) -> None:
        if hash(key) in self.keys:
            index = self.keys.index(hash(key))
            self.values[index]=value
        else:
            self.keys.append(hash(key))
            self.values.append(value)
 
    def get(self, key: int) -> int:
        if hash(key) in self.keys:
            index = self.keys.index(hash(key))
            return self.values[index]
        return -1
        
    def remove(self, key: int) -> None:
        if hash(key) in self.keys:
            index = self.keys.index(hash(key))
            del self.values[index]
            del self.keys[index]


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)