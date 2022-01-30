class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return 0
        
        f_l = max(nums)
        index = nums.index(f_l)
        nums.pop(index)
        s_l = max(nums)
        return index if s_l * 2 <= f_l else -1
        
        
        
                
                
            
                