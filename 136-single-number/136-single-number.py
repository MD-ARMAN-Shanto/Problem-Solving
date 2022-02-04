class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        # counts = {}
        
        # for n in nums:
        # if n not in counts:
        #  counts[n] = 1
        # else :
        # del counts[n]
                
        # return list(counts.keys())[0]
        a = 0
    
        for i in nums:
            a ^= i
        return a
                
            
            
                
                
            
            
