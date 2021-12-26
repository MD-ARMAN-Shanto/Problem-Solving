class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
#         res = [0]
#         total = 0
        
#         for num in range(len(gain)):
#             total += gain[num]
#             res.append(total)
        
#         return max(res)

        alt = 0
        highest = 0
        
        for i in gain:
            alt += i
            
            if alt>highest:
                highest = alt
                
        return highest
        