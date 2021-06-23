# kata: https://www.urionlinejudge.com.br/judge/pt/problems/view/2728

def main():
    while True:
        try:
            response = solution(text=input())
            print(response)
        except EOFError:
            break


def solution(text: str) -> str:
    words = text.split('-')
    is_bug = False

    for i in range(len(words)):
        is_bug = check_bug(words[i], i)
        if is_bug:
            return "BUG"

    return "GRACE HOPPER"


def check_bug(word: str, index: int) -> bool:
    letters = ['c', 'o', 'b', 'o', 'l']
    letter = letters[index]
    initial = word[0].lower()
    ending = word[-1].lower()
    return letter not in (initial, ending)
