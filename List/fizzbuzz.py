
#process 1
def fizz_buzz(number: int) -> str:

    if number % 3 == 0 and number % 5 == 0:
        return 'FizzBuzz'
    elif number % 3 == 0:
        return 'Fizz'
    elif number % 5 == 0:
        return 'Buzz'

    return str(number)


# process 2
def fizz_buzz1(n: int) -> str:

    x, y = n % 3, n % 5

    # if not x and not y:
    #     return 'FizzBuzz'
    # return 'Fizz' if not x else 'Buzz' if not y else str(n)

    # # one line solution
    # return 'FizzBuzz' if not x and not y else ('Fizz' if not x else 'Buzz' if not y else str(n))

if __name__ == '__main__':
    while True:
        print(fizz_buzz1(int(input())))