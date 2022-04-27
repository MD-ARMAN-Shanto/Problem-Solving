class Solution:
    def findWords(self, wds: List[str]) -> List[str]:
        st = {'q': 1, 'w': 1, 'e': 1, 'r': 1, 't': 1, 'y': 1, 'u': 1, 'i': 1, 'o': 1, 'p': 1, 'a': 2, 's': 2, 'd': 2, 'f': 2, 'g': 2, 'h': 2, 'j': 2, 'k': 2, 'l': 2, 'z': 3, 'x': 3, 'c': 3, 'v': 3, 'b': 3, 'n': 3, 'm': 3}

        ret = []

        for wd in wds:
            val = 0
            for i in range(len(wd)):
                if i == 0:
                    val = st.get(wd[i].lower())
                else:
                    if val != st.get(wd[i].lower()):
                        val = -1
                        break
            if val != -1:
                ret.append(wd)
        return ret