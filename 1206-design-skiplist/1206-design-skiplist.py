class Skiplist:

    def __init__(self):
        self.list = []
        

    def search(self, target: int) -> bool:
        self.list.sort()
        start = 0
        end = len(self.list) - 1
        
        while start <= end:
            mid = (start+end)//2
            
            if self.list[mid] == target:
                return True
            elif self.list[mid] < target:
                start = mid + 1 
            else:
                end = mid - 1

        

    def add(self, num: int) -> None:
        self.list.append(num)
        

    def erase(self, num: int) -> bool:
        self.list.sort()
        
        for i in range(len(self.list)):
            if num == self.list[i]:
                self.list.pop(i)
                return True

        


# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)