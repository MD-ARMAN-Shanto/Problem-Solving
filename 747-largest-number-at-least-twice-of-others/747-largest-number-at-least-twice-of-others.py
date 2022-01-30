class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        
        m = max(nums)
        index = nums.index(m)
        
        for num in nums:
            if not m >= 2 * num and m!=num:
                return -1
        else:
            return index
        
        
                
                
            
                