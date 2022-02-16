class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        d = {}
        
        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1
                
        for i, v in d.items():
            if v > 1:
                return True
            
        return False
        