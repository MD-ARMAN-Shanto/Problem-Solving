class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        
        even_arr = []
        odd_arr = []
        
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                even_arr.append(nums[i])
            else:
                odd_arr.append(nums[i])
                
        res = []
        for j in range(len(even_arr)):
            res.append(even_arr[j])
            res.append(odd_arr[j])
            
        return res