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
        if is_bug: return "BUG"

    return "GRACE HOPPER"


def check_bug(letter: str, index: int) -> bool:
    letters = ['c', 'o', 'b', 'o', 'l']
    initial = letter[0].lower()
    ending = letter[-1].lower()
    return letters[index] not in (initial, ending)
