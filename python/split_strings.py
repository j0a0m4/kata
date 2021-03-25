def compose(*functions):
    from functools import reduce
    return reduce(lambda f, g: lambda x: f(g(x)), functions, lambda x: x)


def solution(s: str) -> list:
    return compose(splitPair, addUnderscore)(s)


def splitPair(s: str) -> list:
    buf = []
    for i in range(0, len(s), 2):
        cut = s[i: i + 2]
        buf.append(cut)
    return buf


def addUnderscore(s: str) -> str:
    return (
        s+"_"
        if compose(isOdd, len)(s)
        else s
    )


def isOdd(i: int) -> bool:
    return i % 2 != 0


tests = (
    ("", []),
    ("asdfads", ['as', 'df', 'ad', 's_']),
    ("asdfadsf", ['as', 'df', 'ad', 'sf']),
    ("x", ["x_"]),
)

for inp, exp in tests:
    actual = solution(inp)
    assert actual == exp, "fail"
