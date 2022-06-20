class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        for i, v in enumerate(arr):
            if v > i + k:
                return i + k
            
        return len(arr) + k
            
                
                
            