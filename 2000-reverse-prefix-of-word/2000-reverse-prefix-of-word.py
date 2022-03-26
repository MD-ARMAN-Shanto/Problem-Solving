class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        
        w_list = list(word)
        start = 0
        end = 0
        
        
        while end < len(w_list):
            
            if w_list[end] == ch:
                while start < end:
                    w_list[start], w_list[end] = w_list[end], w_list[start]
                    start += 1
                    end -= 1
                break
            end += 1
            
        return ''.join(w_list)