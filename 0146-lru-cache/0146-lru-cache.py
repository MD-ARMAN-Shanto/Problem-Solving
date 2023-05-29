from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache_dict = OrderedDict()
        

    def get(self, key: int) -> int:
        if key not in self.cache_dict:
            return -1
        else:
            self.cache_dict[key] = self.cache_dict.pop(key)
            return self.cache_dict[key]
        

    def put(self, key: int, value: int) -> None:
        if key not in self.cache_dict:
            if len(self.cache_dict) == self.capacity:
                self.cache_dict.popitem(last=False)
        else:
            self.cache_dict.pop(key)
        self.cache_dict[key] = value
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)