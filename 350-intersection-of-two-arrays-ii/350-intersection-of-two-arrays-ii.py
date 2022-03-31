class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        d = {}
        
        for num in max(nums1, nums2):
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1
            
        res = []
        for num in min(nums1, nums2):
            if num in d and d[num] > 0:
                res.append(num)
                d[num] -= 1
                
        return res