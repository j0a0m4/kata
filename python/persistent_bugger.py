# kata: https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec/train/python

def persistence(n: int, count = 0) -> int:
    return (
        count if n <= 9
        else persistence(multiply_digits(n), count + 1)
    )


def multiply_digits(n: int) -> int:
    adder = 1
    for digit in str(n):
        adder *= int(digit)
    return adder


cases = [(39, 3), (4, 0), (25, 2), (999, 4)]

for case, expected in cases:
    assert persistence(case) == expected, "error"
