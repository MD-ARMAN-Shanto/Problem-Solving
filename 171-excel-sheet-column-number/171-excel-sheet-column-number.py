class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        
        res = 0
        
        for column in columnTitle:
            res = res*26 + ord(column) - ord('A') + 1
            
        return res
