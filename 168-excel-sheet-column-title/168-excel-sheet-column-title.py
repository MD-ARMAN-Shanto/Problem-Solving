class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        
        res = []
        
        while columnNumber > 0:
            columnNumber -= 1
            char = chr(columnNumber % 26 + 65)
            res.insert(0, char)
            columnNumber //= 26
        
        return ''.join(res)
        