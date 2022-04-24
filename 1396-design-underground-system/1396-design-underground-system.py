class UndergroundSystem:

    def __init__(self):
        # customerId: (time, stationName)
        
        self.i = defaultdict(tuple)
        
        # (start, end): timeend - timestart
        self.out = defaultdict(list)
        
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.i[id] = (t, stationName)
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        time, startStation = self.i[id]
        total_time = t - time
        self.out[(startStation, stationName)].append(total_time)
        
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        
        return sum(self.out[(startStation, endStation)]) / len(self.out[(startStation, endStation)])
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)