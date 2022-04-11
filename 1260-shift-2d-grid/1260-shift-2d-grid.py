class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        
        M, N = len(grid), len(grid[0]) # take number of rows and number of columns
        
        # making 2D to 1D 
        def posToVal(r, c):
            return r * N + c
        
        # making 1D to 2D matrix
        def valToPos(v):
            return [ v // N, v % N] # 1st making row then column
        
        res = [[0] * N for i in range(M)]
        
        for r in range(M):
            for c in range(N):
                newVal = (posToVal(r, c) + k) % (M * N) # for not raising bound error
                row, column = valToPos(newVal)
                res[row][column] = grid[r][c]
                
        return res
            
        
        