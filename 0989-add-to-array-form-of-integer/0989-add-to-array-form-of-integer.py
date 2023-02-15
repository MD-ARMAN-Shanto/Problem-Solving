class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        
        result = 0
        
        for digit in num:
            result = 10 * result + digit
            
#         result += k
#         result_array = []
        
#         while result:
#             d = result % 10
#             result_array.append(d)
#             result //= 10
            
#         return result_array[::-1]
    
        return [int(x) for x in str(result+k)]
    
    
    
    
    
    
    