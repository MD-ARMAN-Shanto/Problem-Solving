class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = [1] * len(nums)
        
        prefix = 1  #initial prefix
        for i in range(len(nums)):
            res[i] = prefix # set prefix in res list
            prefix *= nums[i] # multiply every prefix after iteration
        
        postfix = 1
        for i in range(len(nums) - 1, -1 , -1): # from the end
            res[i] *= postfix # multiply res[i] value already exists in the list with postfix
            postfix *= nums[i] # multiply postfix with value in every iteration

        return res
        
            
        