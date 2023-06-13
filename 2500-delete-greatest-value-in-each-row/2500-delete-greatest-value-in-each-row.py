class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        
        res = 0
        
        n = len(grid[0])
        
        for i in range(n):
            max_val = 0
            
            for j in grid:
                new = max(j)
                max_val = max(new, max_val)
                j.remove(new)
                
            res += max_val
                
        return res
            