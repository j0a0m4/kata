# kata: https://www.codewars.com/kata/552c028c030765286c00007d

def iq_test(numbers):
    nums = [int(num) for num in numbers.split(" ")]
    predicate = getPredicate(nums)
    for num in nums:
        if predicate(num):
            return nums.index(num) + 1


def isEven(number):
    return int(number) % 2 == 0


def isOdd(number):
    return not isEven(number)


def getPredicate(numbers):
    even = [num for num in numbers if isEven(num)]
    return (
        isEven if len(even) == 1
        else isOdd
    )


assert iq_test("2 4 7 8 10") == 3, "assert"
assert iq_test("1 2 2") == 1, "assert"
