from typing import List


class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        
        # a1, a2, a3 = set(nums1), set(nums2), set(nums3)
        # return a&a2 | a2&a3 | a1&a3
        # res = {}
        #
        # for i in a1:
        #     if i not in res:
        #         res[i] = 1
        #     else:
        #         res[i] += 1
        #
        # for i in a2:
        #     if i not in res:
        #         res[i] = 1
        #     else:
        #         res[i] += 1
        #
        # for i in a3:
        #     if i not in res:
        #         res[i] = 1
        #     else:
        #         res[i] += 1
        #
        #
        # arr = []
        #
        # for key, value in res.items():
        #     if value >= 2:
        #         arr.append(key)
        #
        # return arr

        ret = []

        ret += set(nums1).intersection(set(nums2))
        ret += set(nums1).intersection(set(nums3))
        ret += set(nums2).intersection(set(nums3))

        return set(ret)

        