class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        
#         d = {}
        
#         for candy in candyType:
#             if candy not in d:
#                 d[candy] = 1
#             else:
#                 d[candy] += 1
        
#         count = min(d, key=d.get)
#         res = []
#         for i, v in d.items():
#             if v == count:
#                 res.append(i)
#             else:

        l = len(candyType) // 2
    
        res = list(set(candyType))
        
        return (len(res[:l]))
                
                
            