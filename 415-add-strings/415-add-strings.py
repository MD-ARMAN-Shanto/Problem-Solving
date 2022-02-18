class Solution:
    
    def helper(self, number: str) -> int:
        
        intDict = {
            "0": 0,
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9
        }
        
        num = 0
        for n in number:
            num *= 10
            num += intDict[n]
            
        return num
            
        
        
    def addStrings(self, num1: str, num2: str) -> str:
        
        return str(self.helper(num1) + self.helper(num2))
        
        
        
        
