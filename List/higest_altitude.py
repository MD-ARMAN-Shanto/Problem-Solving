# leetcode problem number: 1732
"""There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes. The biker
starts his trip on point 0 with altitude equal 0.

You are given an integer array gain of length n where gain[i] is the net gain in altitude between points i and i + 1
for all (0 <= i < n). Return the highest altitude of a point.

test case 1:
    Input: gain = [-5,1,5,0,-7]
    Output: 1
    Explanation: The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.
test case 2:
    Input: gain = [-4,-3,-2,-1,4,3,2]
Output: 0
Explanation: The altitudes are [0,-4,-7,-9,-10,-6,-3,-1]. The highest is 0.
"""

"""
pseudo code:
    alt, max = 0, 0
    
    loop thru the gain:
        add alt value with gain values
        check alt is greater than max
        if true update max value
        then return max
"""
from typing import List
import time


def highestAltitude(gain: List[int]) -> int:

    # first approach
    start = time.time()
    alt, max = 0, 0

    for i in gain:
        alt += i
        if alt > max:
            max = alt
    end = time.time()
    print(f"Runtime of the program is {end - start}")
    return max

    #2nd approach
    # start = time.time()
    # res, total = [0], 0
    #
    # for i in gain:
    #     total += i
    #     res.append(total)
    #
    # end = time.time()
    # print(f"Runtime of the program is {end - start}")
    # return max(res)


if __name__ == '__main__':
    gain = [-5, 1, 5, 0, -7]
    fc = highestAltitude(gain)
    expected_result = 1
    assert expected_result == fc, fc
    print(fc)

    gain = [-5, 1, 5, 0, -7, -3, -4, 5, -3, 1, -10, 8, -5]
    fc = highestAltitude(gain)
    expected_result = 1
    assert expected_result == fc, fc
    print(fc)


