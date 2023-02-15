class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        
        result = 0
        
        for digit in num:
            result = 10 * result + digit
    
        return [int(x) for x in str(result+k)]
    
    
    
    
    
    
    