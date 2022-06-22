class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        zeroCount = 0
        i, result = 0, 0
    
        
        for j in range(len(nums)):
            if nums[j] == 0:
                zeroCount += 1
            while zeroCount > k:
                if nums[i] == 0:
                    zeroCount -= 1
                i += 1
            result = max(result, j-i+1)
    
        return result
    
        