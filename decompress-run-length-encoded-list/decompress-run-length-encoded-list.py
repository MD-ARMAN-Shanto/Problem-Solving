class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        
        res = list()
        for i in range(0, len(nums), 2):
            a = nums[i] * [nums[i+1]]
            res += a
            
        return res
        
        
        
    