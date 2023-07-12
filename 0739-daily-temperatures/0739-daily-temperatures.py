class Solution:
    def dailyTemperatures(self, temp) -> list:
        
        result = [0] * len(temp)
        stack = []
        
        for i, j in enumerate(temp):
            while stack and temp[stack[-1]] < temp[i]:
                index = stack.pop()
                result[index] = (i-index)
            
            stack.append(i)
        
        return result