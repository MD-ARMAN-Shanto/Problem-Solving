class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        
        for num in nums:
            if original == num:
                original = num * 2
            for i in nums:
                if original == i:
                    original = i * 2
                    continue
        return original 
        