class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        
        M, N = len(matrix), len(matrix[0]) # row and colums length
        
        for r in range(M):
            for c in range(N):
                if (matrix[r][c] in rows[r] or
                    matrix[r][c] in cols[c]):
                    
                    return False
                else:
                    rows[r].add(matrix[r][c])
                    cols[c].add(matrix[r][c])
                    
        return True
        