class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        i, j = 0, 0
        s, mx = 0, -2143234345
        
        while j < len(nums):
            s += nums[j]
            
            if j - i + 1 < k:
                j += 1
            else:
                mx = max(mx, s)
                s -= nums[i]
                i += 1
                j += 1
                
        return mx/k