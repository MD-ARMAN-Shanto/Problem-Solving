class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        
        res1 = ''.join(word1)
        res2 = ''.join(word2)
        
        if res1 != res2:
            return False
        
        return True
        