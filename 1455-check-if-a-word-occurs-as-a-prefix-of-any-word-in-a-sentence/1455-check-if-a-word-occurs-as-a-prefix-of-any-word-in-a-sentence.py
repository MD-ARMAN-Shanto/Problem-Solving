class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        
        l = sentence.split(' ')
        res = []
        
        for word in l:
            if len(word) >= len(searchWord):
                val = word[:len(searchWord)]
                res.append(val)
            else:
                res.append(word)
        
        for ch in range(len(res)):
            if res[ch] == searchWord:
                return ch + 1
                
        return -1
            
            
        