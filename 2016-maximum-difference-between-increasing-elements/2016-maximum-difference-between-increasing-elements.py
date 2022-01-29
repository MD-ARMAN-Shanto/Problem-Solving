class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        
        i_v = nums[0]
        max_val = 0
        
        for i in range(1, len(nums)):
            
            curr_diff = nums[i] - i_v
            i_v = min(i_v, nums[i])
            
            if curr_diff > max_val:
                max_val = curr_diff
                
        return max_val if max_val > 0 else -1
            
            
                
                
        