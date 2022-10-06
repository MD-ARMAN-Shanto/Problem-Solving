class TimeMap:

    def __init__(self):
        self.d = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.d:
            self.d[key] = {}
            
        self.d[key][timestamp] = value
        
    def get(self, key: str, timestamp: int) -> str:
        if not key in self.d:
            return ""
        
        for curr_time in reversed(range(1, timestamp+1)):
            if curr_time in self.d[key]:
                return self.d[key][curr_time]
            
        return ""
            

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)