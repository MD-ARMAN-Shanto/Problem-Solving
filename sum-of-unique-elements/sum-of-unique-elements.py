class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        
        
        res = {}
        
        for key, val in enumerate(nums):
            if val not in res:
                res[val] = 1
            else:
                res[val] += 1
        
        sum = 0
        for key, value in res.items():
            if value == 1:
                sum += key
        return sum
                