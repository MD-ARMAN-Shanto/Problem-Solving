class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        #rightMax = -1
        # loop thru in reverse order
        # newMax = max(rightMax, arr[i])
        # return the original array
        
        rightMax = -1
        
        for i in range(len(arr)-1, -1, -1):
            newMax = max(rightMax, arr[i])
            arr[i] = rightMax
            rightMax = newMax
            
        return arr
        