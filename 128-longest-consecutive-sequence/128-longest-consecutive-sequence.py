class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        
        nums.sort()
        
        longest_strike = 1
        current_strike = 1 
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                if nums[i] == nums[i-1]+1:
                    current_strike += 1
                else:
                    longest_strike = max(current_strike, longest_strike)
                    current_strike = 1
                    
        return max(longest_strike, current_strike)
       