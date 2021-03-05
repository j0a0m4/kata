# kata: https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39

def num_delegate(x: int, fn): return fn(x) if fn else x


def zero(fn=None): return num_delegate(0, fn)
def one(fn=None): return num_delegate(1, fn)
def two(fn=None): return num_delegate(2, fn)
def three(fn=None): return num_delegate(3, fn)
def four(fn=None): return num_delegate(4, fn)
def five(fn=None): return num_delegate(5, fn)
def six(fn=None): return num_delegate(6, fn)
def seven(fn=None): return num_delegate(7, fn)
def eight(fn=None): return num_delegate(8, fn)
def nine(fn=None): return num_delegate(9, fn)


def plus(y): return lambda x: x + y
def minus(y): return lambda x: x - y
def times(y): return lambda x: x * y
def divided_by(y): return lambda x: x // y


assertions = [
    (seven(times(five())), 35),
    (four(plus(nine())), 13),
    (eight(minus(three())), 5),
    (six(divided_by(two())), 3),
]

for fnCall, expected in assertions:
    assert fnCall == expected, "Assertion failed."
