class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        
        exists = set()
        
        for i in range(len(arr)):
            if arr[i] * 2 in exists or arr[i] / 2 in exists:
                return True
            else:
                exists.add(arr[i])
        
        return False
        

        
                
            
                
