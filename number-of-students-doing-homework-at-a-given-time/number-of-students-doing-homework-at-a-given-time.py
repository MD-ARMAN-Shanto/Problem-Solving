class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        
        count = 0
        
        for time in range(len(startTime)):
            if queryTime >= startTime[time] and queryTime <= endTime[time]:
                count+= 1
        return count
        