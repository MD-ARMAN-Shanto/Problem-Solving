class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        x = nums[:n]
        y = nums[n:2*n]
        
        result = []
        
        for i in range(n):
            result.append(x[i])
            result.append(y[i])
            
        return result
            
        