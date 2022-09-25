class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        
        result = 0
        
        for i in range(len(nums1)):
            count = 0
            
            for (x1, x2) in zip(nums1[i:], nums2):
                if x1 == x2: count += 1
                else:
                    result = max(count, result)
                    count = 0
                    
            result = max(result, count)
            
        for i in range(len(nums2)):
            count = 0
            
            for (x1, x2) in zip(nums2[i:], nums1):
                if x1 == x2: count += 1
                else:
                    result = max(count, result)
                    count = 0
                    
            result = max(result, count)
            
        return result