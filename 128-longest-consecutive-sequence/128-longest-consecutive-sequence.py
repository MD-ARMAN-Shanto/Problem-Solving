class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
    
        # 2nd approch creating subsequece
        
        nSet = set(nums)
        longest = 0
        
        for num in nums:
            #initialize the length of sequence
            length = 0
            # check num-1 value not in set
            if (num-1) not in nSet:
                # check num+length = next_value in set
                while (num+length) in nSet:
                    length += 1
                # assign the longest subsequence value
                longest = max(length, longest)
                
        return longest
                
                
                
                
                
                
                
                
                
                
        
       