from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> List[int]:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    i = m - 1
    j = n - 1
    idx = len(nums1) - 1

    while i >= 0 and j >= 0:
        if nums1[i] >= nums2[j]:
            # nums1.insert(nums1[idx], nums1[i])
            nums1[idx] = nums1[i]
            i -= 1
        else:
            # nums1.insert(nums1[idx], nums2[j])
            nums1[idx] = nums2[j]
            j -= 1
        idx -= 1

    while j >= 0:
        nums1[j] = nums2[j]
        j -= 1

    return nums1

#         nums3 = nums1[:m]
#         nums4 = nums2[:n]

#         res = nums3+nums4
#         res.sort()

#         for i in range(len(res)):
#             nums1[i] = res[i]


if __name__ == '__main__':
    # test case 1
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    m, n = 3, 3
    function_call = merge(nums1=nums1, m=m, nums2=nums2, n=n)
    expected_result = [1, 2, 2, 3, 5, 6]
    assert expected_result == function_call, function_call
    print(function_call)

    # test case 2
    nums1 = [1]
    nums2 = []
    m, n = 1, 0
    function_call = merge(nums1=nums1, m=m, nums2=nums2, n=n)
    expected_result = [1]
    assert expected_result == function_call, function_call
    print(function_call)

    # test case 3
    nums1 = [0]
    nums2 = [5]
    m, n = 0, 1
    function_call = merge(nums1=nums1, m=m, nums2=nums2, n=n)
    expected_result = [5]
    assert expected_result == function_call, function_call
    print(function_call)

    # test case 4
    nums1 = []
    nums2 = []
    m, n = 0, 0
    function_call = merge(nums1=nums1, m=m, nums2=nums2, n=n)
    expected_result = []
    assert expected_result == function_call, function_call
    print(function_call)









