class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        d = {}
        
        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1
                
        for i, v in d.items():
            if v > 1:
                return i