# kata: https://www.codewars.com/kata/559536379512a64472000053

from string import ascii_lowercase as alphabet
from functools import reduce, partial


def play_pass(s, n):
    shifter = partial(shift, n)
    mapper = compose(reverse, complement, case, shifter)
    return mapper(s)


def compose(*functions):
    return reduce(lambda f, g: lambda x: f(g(x)), functions, lambda x: x)


def reverse(word):
    return "".join(word[::-1])


def complement(word):
    return "".join([
        nine_complement(char)
        if char.isdigit()
        else char
        for char in word
    ])


def nine_complement(digit):
    return str(9 - int(digit))


def shift(n, word):
    return "".join([
        shift_letter(char, n)
        if char.isalpha()
        else char
        for char in word
    ])


def shift_letter(word, n):
    idx = alphabet.index(word.lower())
    idx += n
    idx = idx % len(alphabet)
    return alphabet[idx]


def case(word):
    buf = ""
    for i in range(0, len(word)):
        char = word[i]
        if not char.isalpha():
            buf += char
            continue
        if isEven(i):
            buf += char.upper()
            continue
        buf += char.lower()
    return buf


def isEven(num): return num % 2 == 0


assert play_pass("I LOVE YOU!!!", 1) == "!!!vPz fWpM J", "error"

assert play_pass("MY GRANMA CAME FROM NY ON THE 23RD OF APRIL 2015",
                 2) == "4897 NkTrC Hq fT67 GjV Pq aP OqTh gOcE CoPcTi aO", "error"

# kata: https://www.codewars.com/kata/559536379512a64472000053/
