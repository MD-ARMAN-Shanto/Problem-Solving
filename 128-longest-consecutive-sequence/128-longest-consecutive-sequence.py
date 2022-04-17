class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
            
        nSet = set(nums)
        longest = 0
        
        for num in nums:
            
            if (num-1) not in nSet:
                length = 1
                while (num+length) in nSet:
                    length += 1
                longest = max(length, longest)
                
        return longest
                
                
                
                
                
                
                
                
                
                
        
       