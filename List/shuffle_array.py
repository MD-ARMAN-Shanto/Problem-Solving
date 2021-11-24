"""
Prog: Md. Arman Hossain
site: Leetcode
Type: List
"""
from typing import List


def shuffle(nums: List[int], n: int) -> List[int]:
    nums1 = nums[:n]
    nums2 = nums[n:]

    nums[::2] = nums1
    nums[1::2] = nums2

    return nums


#         res = []

#         i = 0
#         j = 0

#         for i in range(n):
#             res.append(nums1[i])
#             res.append(nums2[i])

#         return res

#         res = []

#         for i in range(n):
#             res += [nums[i], nums[i+n]]

#         return res

if __name__ == '__main__':
    nums = [2, 5, 1, 3, 4, 7]
    n = 3
    fc = shuffle(nums, n)
    expected_result = [2, 3, 5, 4, 1, 7]
    assert expected_result == fc, fc
    print(fc)

    nums =[1, 2, 3, 4, 4, 3, 2, 1]
    n = 4
    fc = shuffle(nums, n)
    expected_result = [1, 4, 2, 3, 3, 2, 4, 1]
    assert expected_result == fc, fc
    print(fc)


