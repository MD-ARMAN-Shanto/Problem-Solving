"""
Prog: Md. Arman Hossain
site: Leetcode
Type: List
"""

from typing import List


def buildArray(nums: List[int]) -> List[int]:
    res = list()

    for i in range(len(nums)):
        res.append(nums[nums[i]])

    return res


if __name__ == '__main__':
    nums = [0, 2, 1, 5, 3, 4]
    fc = buildArray(nums)
    expected_result = [0, 1, 2, 4, 5, 3]
    assert expected_result == fc, fc
    print(fc)

    nums = [5, 0, 1, 2, 3, 4]
    fc = buildArray(nums)
    expected_result = [4, 5, 0, 1, 2, 3]
    assert expected_result == fc, fc
    print(fc)