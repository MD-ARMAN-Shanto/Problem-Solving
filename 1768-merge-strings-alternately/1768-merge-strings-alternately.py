class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res=''
        min_val = min(len(word1),len(word2))
        for i in range(min_val):
            res += word1[i] + word2[i]

        return res + word1[i+1:] + word2[i+1:]