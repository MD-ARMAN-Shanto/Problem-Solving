class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        
        a1, a2, a3 = set(nums1), set(nums2), set(nums3)
        res = {}
        
        for i in a1:
            if i not in res:
                res[i] = 1
            else:
                res[i] += 1
                
        for i in a2:
            if i not in res:
                res[i] = 1
            else:
                res[i] += 1 
                
        for i in a3:
            if i not in res:
                res[i] = 1
            else:
                res[i] += 1
                
        
        arr = []
        
        for key, value in res.items():
            if value >= 2:
                arr.append(key)
                
        return arr
        
        
            
        