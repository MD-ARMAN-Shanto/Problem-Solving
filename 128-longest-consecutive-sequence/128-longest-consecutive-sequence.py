class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
            
        nSet = set(nums)
        longest = 0
        
        for num in nums:
            length = 0
            if (num-1) not in nSet:
                while (num+length) in nSet:
                    length += 1
                longest = max(length, longest)
                
        return longest
                
                
                
                
                
                
                
                
                
                
        
       