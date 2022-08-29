class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid:
            return 0
        
        #count the island
        count = 0
        
        # loop through the grid with i, j
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1
                    
        return count
    
    
    def dfs(self, grid, x, y):
        
        # handle the boundary limit 
        if x<0 or y<0 or x>=len(grid) or y>=len(grid[0]) or grid[x][y] != '1':
            return 
        
        # marking the land already visited
        grid[x][y] = '2'
        self.dfs(grid, x+1, y)
        self.dfs(grid, x-1, y)
        self.dfs(grid, x, y+1)
        self.dfs(grid, x, y-1)
        
        
        
        
        
        
        
        
        
        
                    