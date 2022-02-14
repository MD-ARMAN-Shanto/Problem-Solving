class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        dic = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        result = [""]
        
        if digits == "":
            return []
        
        for d in digits:
            result = [r+i for r in result for i in dic[d]]
            
        return result
                      
                