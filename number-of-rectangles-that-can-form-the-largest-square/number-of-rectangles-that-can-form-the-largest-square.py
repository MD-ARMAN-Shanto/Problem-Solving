class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        
        res = []
        max_value = 0
        
        for rectangle in rectangles:
            min_value = min(rectangle)
            res.append(min_value)
            max_value = max(min_value, max_value)
            
        return res.count(max_value)
            
            
            
        