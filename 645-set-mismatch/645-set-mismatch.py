class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        nums.sort()
        
        seen = set()
        res = []
        
        for num in nums:
            if num in seen:
                res.append(num)
            seen.add(num)
        
        set_l = set(nums)
        for i in range(1, len(nums)+1):
            if i not in set_l:
                res.append(i)
                break
                
        return res
        