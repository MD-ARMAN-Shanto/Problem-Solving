class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set) #it will be key pair key(r//3, c//3), for checking 3*3 matrix
        
        for r in range(9): #it's only have 9 rows
            for c in range(9): # 9 column as well
                
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r//3, c//3)]):
                    
                    return False
                else:
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    squares[(r//3, c//3)].add(board[r][c])
                    
        return True
                