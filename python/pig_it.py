# kata: https://www.codewars.com/kata/520b9d2ad5c005041100000f/train/python

from string import punctuation


def pig_it(text):
    words = text.split(' ')
    return " ".join([
        transform(word)
        for word in words
    ])


def transform(word):
    if word in punctuation:
        return word
    else:
        return word[1:] + word[0] + 'ay'


tests = [
    ('Pig latin is cool', 'igPay atinlay siay oolcay'),
    ('This is my string', 'hisTay siay ymay tringsay'),
    ('Hello world !', 'elloHay orldway !')
]

for argument, expected in tests:
    actual = pig_it(argument)
    assert actual == expected, f"pig_it({argument}) \n expected {expected}. actual is {actual}."
