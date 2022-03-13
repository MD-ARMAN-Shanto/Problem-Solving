class Solution:
    def nearestValidPoint(self, x1: int, y1: int, points: List[List[int]]) -> int:
        
        result = -1
        mini = 4294967296
        
        for i in range(len(points)):
            if points[i][0]==x1 or points[i][1]==y1:
                run_total = abs(x1-points[i][0]) + abs(y1-points[i][1])

                if run_total < mini:
                    mini = run_total
                    result = i
                    
        return result if result >= 0 else -1
                    
                    