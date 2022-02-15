class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        max_area = 0
        
        start = 0
        end = len(height) - 1
        
        while start < end:
            
            area = (end-start) * min(height[end], height[start])
            max_area = max(max_area, area)
            
            if height[end] > height[start]:
                start += 1
            else:
                end -= 1
            
        return max_area