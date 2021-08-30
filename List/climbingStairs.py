# function solution for climbing any stair with 1 or 2 unique moves.

def climbing_stairs(steps: int) -> int:

    if steps <= 3:
        output = steps
    else:
        last_step = 3
        before_last_step = 2
        i = 3

        while i < steps:
            output = last_step + before_last_step
            before_last_step = last_step
            last_step = output
            i += 1

        return output


if __name__ == '__main__':
    input = 7
    func_call = climbing_stairs(input)
    expected_result = 21
    assert expected_result == func_call, func_call
    print(func_call)


# solution 2 using class based with memoization

class Climbing:
    def climbing_stairs(self, n: int) -> int:
        memo = [None] * (n + 1)
        return self._helper(n, memo)

    def _helper(self, n, memo):
        if n < 0:
            return 0
        if n == 1 or n == 0:
            return 1
        if memo[n]:
            return memo[n]

        memo[n] = self._helper(n-1, memo) + self._helper(n-2, memo)

        return memo[n]


stair = Climbing()
print(stair.climbing_stairs(7))