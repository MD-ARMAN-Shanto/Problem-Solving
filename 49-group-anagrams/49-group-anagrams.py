class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
#         result = collections.defaultdict(list) # {} normal dict doesn't allow list value that's why                                                         using tuple with defaultdict
#         for s in strs:
#             count = [0] * 26 #count all the character in word

#             for c in s:
#                 count[ord(c) - ord("a")] += 1
#             result[tuple(count)].append(s)

#         return result.values() 

        h = {}
        for word in strs:
            sortedWord = ''.join(sorted(word))
            if sortedWord not in h:
                h[sortedWord] = [word]
            else:
                h[sortedWord].append(word)
        final = []
        for value in h.values():
            final.append(value)
        return final
        