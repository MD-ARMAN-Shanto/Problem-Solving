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

        unique_candies = len(set(candyType))
        l = len(candyType) // 2
    
        return min(unique_candies, l)
        
    
#         res = list(set(candyType))
        
#         return (len(res[:l]))
                
                
            