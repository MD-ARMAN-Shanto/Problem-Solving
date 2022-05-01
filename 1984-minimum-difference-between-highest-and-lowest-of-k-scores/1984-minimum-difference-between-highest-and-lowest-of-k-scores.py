class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        res = []
        
        i, j = 0, k-1
        mindiff = float('inf')
        
        while j < len(nums):
            mindiff = min(mindiff, nums[j] -  nums[i]) 
            res.append(mindiff)
            i, j = i + 1, j + 1
                
        return mindiff

                    
                    
        