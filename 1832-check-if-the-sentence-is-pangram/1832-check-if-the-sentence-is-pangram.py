class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        
        ascii_val = [_ for _ in range(97, 123)]
        sentence_ascii = []
        
        for ch in sentence:
            sentence_ascii.append(ord(ch))
            
        if not len(ascii_val) == len(set(sentence_ascii)):
            return False
        
        return True
        
        