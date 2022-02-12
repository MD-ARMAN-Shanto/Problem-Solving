class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        
        index = 0
        
        while index < len(arr):
            if arr[index] == 0:
                arr.insert(index+1, 0)
                arr.pop()
                index += 2
            else:
                index += 1