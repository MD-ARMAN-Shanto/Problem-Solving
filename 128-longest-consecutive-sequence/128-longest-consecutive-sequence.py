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
    
        # 2nd approch creating subsequece
        
#         nSet = set(nums)
#         longest = 0
        
#         for num in nums:
#             length = 0
#             # check num-1 value not in set
#             if (num-1) not in nSet:
#                 length += 1
#                 # check num+length = next_value in set
#                 while (num+length) in nSet:
#                     length += 1
#                 # assign the longest subsequence value
#                 longest = max(longest, length)
                
#         return longest
                
                
                
                
                
                
                
                
                
                
        
       