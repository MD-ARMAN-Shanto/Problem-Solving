"""
you are given a list of integers and you need to find the sublist of the list

example 1:
nums = [1, 5]
result = [[], [1], [5], [1,5]]
"""
from typing import List


def sublist(nums: List[int]) -> List[List[int]]:

    result = [[]]

    for i in range(len(nums) + 1):
        for j in range(i):
            result.append(nums[j:i])
    return result


if __name__ == '__main__':
    mat = [1, 5]
    fc = sublist(mat)
    expected_result = [[], [1], [1, 5], [5]]
    assert expected_result == fc, fc
    print(fc)

