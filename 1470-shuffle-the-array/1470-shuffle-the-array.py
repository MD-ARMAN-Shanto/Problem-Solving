class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        x = nums[:n]
        y = nums[n:2*n]
        
        result = []
        
        for i, j in zip(x,y):
            result.append(i)
            result.append(j)
            
        return result
            
        