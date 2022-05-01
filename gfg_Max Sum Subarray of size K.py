"""Max Sum Subarray of size K
Basic Accuracy: 52.08% Submissions: 22709 Points: 1
Given an array of integers Arr of size N and a number K. Return the maximum sum of a subarray of size K"""


def maximumSumSubarray (arr, N, k):
    i, j = 0, 0
    s, mx = 0, 0

    while j < n:
        s += arr[j]

        if j - i + 1 < k:
            j += 1
        else:
            mx = max(mx, s)
            s -= arr[i]
            i += 1
            j += 1
    return mx


if __name__ == "__main__":
    arr, n, k = [100, 200, 300, 400], 4, 2
    expected_result = 700
    final_result = maximumSumSubarray(arr, n, k)
    assert expected_result == final_result, final_result
    print(final_result)

if __name__ == "__main__":
    arr, n, k = [100, 200, 300, 400], 4, 4
    expected_result = 1000
    final_result = maximumSumSubarray(arr, n, k)
    assert expected_result == final_result, final_result
    print(final_result)