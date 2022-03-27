class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        d = {}
        
        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1
                
        
        res = []
        for i, k in d.items():
            if k > 1:
                res.append(i)
                
        return res
                