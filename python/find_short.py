# kata: https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9

from functools import reduce
from sys import maxsize


def find_short(s: str) -> int:
    return reduce(min_len_reducer, s.split(" "), maxsize)


def min_len_reducer(minLen: int, word: str):
    return minLen if minLen < len(word) else len(word)


assertions = [
    ("bitcoin take over the world maybe who knows perhaps", 3),
    ("turns out random test cases are easier than writing out basic ones", 3),
    ("lets talk about javascript the best language", 3),
    ("i want to travel the world writing code one day", 1),
    ("Lets all go on holiday somewhere very cold", 2),
]

for sample, expected in assertions:
    assert find_short(sample) == expected, "Assertion Fail"
