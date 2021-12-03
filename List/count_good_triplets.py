from typing import List


def countGoodTriplets(arr: List[int], a: int, b: int, c: int) -> int:
    count = 0

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            for k in range(j + 1, len(arr)):
                if abs(arr[i]-arr[j]) <= a and abs(arr[j]-arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                    count += 1
    return count


if __name__ == '__main__':

    li = [3, 0, 1, 1, 9, 7]
    a, b, c = 7, 2, 3
    fc = countGoodTriplets(li, a, b, c)
    expected_result = 4
    assert expected_result == fc, fc
    print(fc)