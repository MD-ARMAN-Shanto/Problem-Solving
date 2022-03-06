class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        
        t_odd_f = False
        
        for i in range(len(arr)-2):
            
            mod = arr[i] % 2
            mod1 = arr[i+1] % 2
            mod2 = arr[i+2] % 2
            
            if mod and mod1 == 1 and mod and mod2 == 1:
                t_odd_f = True
                
        return t_odd_f