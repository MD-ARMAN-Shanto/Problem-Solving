class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
        d = {}
        
        for word in words[0]:
            d[word] = d.get(word, 0) + 1
                    
        for x in d:
            for i in range(1, len(words)):
                if x in words[i]:
                    d[x] = min(d[x], words[i].count(x))
                else:
                    d[x] = 0
                    break
                            
        ans = []
        
        for i, v in d.items():
            ans += v * [i]
                    
        return ans
                        
        