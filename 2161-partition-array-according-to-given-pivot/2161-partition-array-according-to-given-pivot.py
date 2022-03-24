class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        
        idx = 0
        p_l = []
        
        
        for num in nums:
            if num < pivot:
                p_l.append(num)
            idx += 1
            
        for num in nums:
            if num == pivot:
                p_l.append(pivot)
            idx += 1
            
        for num in nums:
            if num > pivot:
                p_l.append(num)
            idx += 1
                
        return p_l
                