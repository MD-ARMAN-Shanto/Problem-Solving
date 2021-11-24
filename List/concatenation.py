"""
Prog: Md. Arman Hossain
site: Leetcode
Type: List
"""

from typing import List


def getConcatenation(nums: List[int]) -> List[int]:
    return nums + nums


if __name__ == '__main__':
    nums = [0, 2, 1, 5, 3, 4]
    fc = getConcatenation(nums)
    expected_result = [0, 2, 1, 5, 3, 4, 0, 2, 1, 5, 3, 4]
    assert expected_result == fc, fc
    print(fc)

    nums = [5, 0, 1, 2, 3, 4]
    fc = getConcatenation(nums)
    expected_result = [5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4]
    assert expected_result == fc, fc
    print(fc)