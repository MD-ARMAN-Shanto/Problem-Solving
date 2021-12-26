class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        
        matrix = []
        count = 0
        
        for i in range(m):
            l = []
            for j in range(n):
                l.append(0)
            matrix.append(l[:])
                
        for r, c in indices:
            for k in range(n):
                matrix[r][k]+=1
            
            for z in range(m):
                matrix[z][c] += 1
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] %2 !=0:
                    count += 1
        
        return count 
                
        

            
            
                
                
            
                
        