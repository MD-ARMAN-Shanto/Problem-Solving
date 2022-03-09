class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        
        len_count = 0
        
        for word in sentences:
            split_word = word.split(' ')
            len_split_word = len(split_word)
            
            if len_split_word > len_count:
                len_count = len_split_word
                
        return len_count