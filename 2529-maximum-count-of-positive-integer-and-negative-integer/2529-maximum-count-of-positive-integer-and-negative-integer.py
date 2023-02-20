class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        
        max_count, pos_count, neg_count = 0, 0, 0
        
        for num in nums:
            if num < 0:
                neg_count += 1
            elif num > 0:
                pos_count += 1
                
            max_count = max(pos_count, neg_count)
            
        return max_count