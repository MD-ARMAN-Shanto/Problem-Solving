class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        
        w1 = Counter(words1)
        w2 = Counter(words2)
        count = 0
        for word in words1:
            if word in words2 and w1[word]==w2[word]==1:
                count+=1
                
        return count

        
        
            
        
        