class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        #rightMax = -1
        # loop thru in reverse order
        # newMax = max(rightMax, arr[i])
        # return the original array
        
        rightIndex = -1
        
        for i in range(len(arr)-1, -1 , -1):
            newMax = max(arr[i], rightIndex)
            arr[i] = rightIndex
            rightIndex = newMax                    
            
        return arr