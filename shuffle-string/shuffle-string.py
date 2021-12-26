class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        
#         res = []
        
#         for i in range(len(indices)):
#             res.append((indices[i], s[i]))
        
#         res.sort()

#         result = ''
#         for pair in res:
#             result += pair[1]
            
            
#         return ''.join(result)
            
    
        res = list(s)
        
        for i in enumerate(indices):
            res[i[1]] = s[i[0]]
            
        return ''.join(res)
            
        
            
            
        
        
        