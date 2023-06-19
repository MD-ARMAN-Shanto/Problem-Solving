class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        total_gain = [0]
        
        for i in range(len(gain)):
            total_gain.append(total_gain[i]+gain[i])
            
        return max(total_gain)
    
#         alt, highest = 0, 0
        
#         for i in gain:
#             alt += i
            
#             if alt>highest:
#                 highest = alt
                
#         return highest