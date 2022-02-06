class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        stack = []
        d = {}
        res = []
        
        for i in range(len(nums2)):
            
            while stack and nums2[stack[-1]] < nums2[i]:
                d[nums2[stack[-1]]] = nums2[i]
                stack.pop()
            stack.append(i)
        
        for num in nums1:
            if num in d.keys():
                res.append(d[num])
            else:
                res.append(-1)
            
        return res
                
                
                
            
            
            
        