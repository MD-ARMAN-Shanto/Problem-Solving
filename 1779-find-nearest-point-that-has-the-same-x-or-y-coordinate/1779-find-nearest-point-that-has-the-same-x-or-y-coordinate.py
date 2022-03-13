class Solution:
    def nearestValidPoint(self, x1: int, y1: int, points: List[List[int]]) -> int:
        
        result = -1
        mini = float(inf)
        
        for i in range(len(points)):
            for x2, y2 in zip(points[i], points[i][1:]):
                
                if x1==x2 or y1==y2:
                    run_total = abs(x1-x2) + abs(y1-y2)
                    
                    if run_total<mini:
                        mini = run_total
                        result = i
                    
        return result if result >= 0 else -1
                    
                    