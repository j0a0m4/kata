from functools import reduce, partial


def compose(*functions):
    return reduce(lambda f, g: lambda x: f(g(x)), functions, lambda x: x)


def solution(s: str) -> list:
    fn = compose(
        split_pair,
        partial(append_underscore, s),
        compose(is_odd, len)
    )
    return fn(s)


def split_pair(s: str) -> list:
    return [extract_pair(s, i) for i in range(0, len(s), 2)]


def extract_pair(s: str, i: int) -> str: return s[i: i + 2]


def add_underscore(s: str) -> str: return s+"_"


def append_underscore(s: str, is_odd: bool) -> str:
    return add_underscore(s) if is_odd else s


def is_odd(i: int) -> bool: return i % 2 != 0


scenarios = (
    ("", []),
    ("asdfads", ['as', 'df', 'ad', 's_']),
    ("asdfadsf", ['as', 'df', 'ad', 's']),
    ("x", ["x_"]),
)

for example, expected in scenarios:
    actual = solution(example)
    warning = f"""FAIL! 
    Case: solution(\"{example}\")
    Expected: {expected}
    Actual: {actual}"""
    assert actual == expected, warning
