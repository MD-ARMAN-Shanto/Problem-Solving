class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        
        if num1== 0 or num2 == 0:
            return 0
        
        count = 0
        
        for i in range(max(num1, num2)):
            if num1 < num2:
                num2 -= num1
            elif num1 > num2:
                num1 -= num2
            else:
                num1 - num2
                break
            count += 1
            
        return count + 1 