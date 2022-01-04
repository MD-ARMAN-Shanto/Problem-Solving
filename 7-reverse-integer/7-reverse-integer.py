class Solution:
    def reverse(self, x: int) -> int:
        if x==0:
            return x
        if x > 0:
            rev = int(str(x)[::-1])
        else:
            rev = int(f'-{str(x)[1:][::-1]}')

        if rev > 2147483648 or rev < -2147483648:
            return 0
        return rev
        