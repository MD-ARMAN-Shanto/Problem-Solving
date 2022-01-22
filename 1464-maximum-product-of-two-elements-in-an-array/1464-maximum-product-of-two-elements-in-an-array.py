class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
#         max_index = nums.index(max(nums))
#         max_1 = nums.pop(max_index)
#         max_2 = max(nums)
        
#         res = (max_1-1) * (max_2-1)
        
#         return res

        first = second = 0
    
        for number in nums:
            if number > first:
                first, second = number, first
            else:
                second = max(number, second)
                
        return (first-1) * (second-1)
        