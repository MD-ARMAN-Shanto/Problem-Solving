class Solution:
    def reverseWords(self, s: str) -> str:
        
        li = s.split(' ')
        
        result = []
        
        for word in li:
            result.append(word[::-1])
            
        return ' '.join(result)
        