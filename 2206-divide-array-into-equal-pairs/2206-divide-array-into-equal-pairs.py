class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        
        d = {}
        
        for num in nums:
            d[num] = d.get(num, 0) + 1
        
        flag = True
        
        for i, k in d.items():
            if k % 2 != 0:
                flag = False
            
        return flag
        