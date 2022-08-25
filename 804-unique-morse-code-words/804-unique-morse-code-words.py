class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        
        morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        res = {}
        a = ''
        count = 1
        s = 0
        for word in words:
            for ch in word:
                a += morse_code[ord(ch)-97]
            
            if a not in res:
                res[a] = count
            a = ''
        
        for value in res.values():
            s += value
        return s
            

                
        
            