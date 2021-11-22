from typing import List


def getConcatenation(nums: List[int]) -> List[int]:

    # process 1
    return nums + nums

    # process 2
    return nums * 2

    # process 3
    nums1 = nums.copy()
    res = nums1 + nums
    return res


if __name__ == '__main__':
    nums1 = [1, 2, 3]
    fc = getConcatenation(nums1)
    expected_result = [1, 2, 3, 1, 2, 3]
    assert expected_result == fc, fc
    print(fc)

    nums1 = [0]
    fc = getConcatenation(nums1)
    expected_result = [0, 0]
    assert expected_result == fc, fc
    print(fc)

    nums1 = []
    fc = getConcatenation(nums1)
    expected_result = []
    assert expected_result == fc, fc
    print(fc)
