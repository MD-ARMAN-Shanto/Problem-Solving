"""
On a 2D plane, there are n points with integer coordinates points[i] = [xi, yi]. Return the minimum time in seconds to visit all the points in the order given by points.

You can move according to these rules:

In 1 second, you can either:
move vertically by one unit,
move horizontally by one unit, or
move diagonally sqrt(2) units (in other words, move one unit vertically then one unit horizontally in 1 second).
You have to visit the points in the same order as they appear in the array.
You are allowed to pass through points that appear later in the order, but these do not count as visits.

Example 1:
Input: points = [[1,1],[3,4],[-1,0]]
Output: 7
Explanation: One optimal path is [1,1] -> [2,2] -> [3,3] -> [3,4] -> [2,3] -> [1,2] -> [0,1] -> [-1,0]
Time from [1,1] to [3,4] = 3 seconds
Time from [3,4] to [-1,0] = 4 seconds
Total time = 7 seconds

Example 2:
Input: points = [[3,2],[-2,2]]
Output: 5
"""
from typing import List


def minTimeToVisitAllPoints(points: List[List[int]]) -> int:
    total_time = 0

    for i in range(len(points) - 1):
        point1 = points[i]
        point2 = points[i + 1]

        x = abs(point2[0] - point1[0])  # calculate x = abs(x2-x1)
        y = abs(point1[1] - point2[1])  # calculate y = abs(y2-y1)

        total_time += max(x, y)

    return total_time


if __name__ == '__main__':
    points = [[1, 1], [3, 4], [-1, 0]]
    func_call = minTimeToVisitAllPoints(points)
    expected_result = 7
    assert expected_result == func_call, func_call
    print(func_call)

    points = [[3, 2], [-2, 2]]
    func_call = minTimeToVisitAllPoints(points)
    expected_result = 5
    assert expected_result == func_call, func_call
    print(func_call)
