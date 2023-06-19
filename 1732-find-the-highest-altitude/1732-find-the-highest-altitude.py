class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        total_gain = [0]
        
        for i in range(len(gain)):
            total_gain.append(total_gain[i]+gain[i])
            
        return max(total_gain)