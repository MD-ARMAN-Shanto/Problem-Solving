class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        visited = set()
        
        def dfs(i, j):
            """
            -- checking row i is out of bound
            -- checking coloum j is out of bound
            -- if row i value is less than 0 also out of bound
            -- if column j value less than 0 also out of bound
            -- last grid[i][j] value equals to 0 means water than 
            
            return 1 as perimeter count
            
            """
            if i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0 or grid[i][j] == 0:
                return 1
            
            # check the row and column already visited then return 0
            if (i, j) in visited:
                return 0
            
            # now add i, j into the visited set so that we don't need to revisit the place twice
            visited.add((i, j))
            
            # now declare the 4 sides recusively 
            perimeter = dfs(i, j+1) # same row next column
            perimeter += dfs(i+1, j) # same column next row
            perimeter += dfs(i, j-1) # checking the previous column of the same row
            perimeter += dfs(i-1, j) # checking the upper row of the same column
            
            return perimeter
            
        
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:              # finding the land in the grid
                    return dfs(i, j)
                
                
                