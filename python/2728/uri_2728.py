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
    result = {predicate(word) for word in words}
    return "GRACE HOPPER" if False not in result else "BUG"


def predicate(word: str) -> bool:
    letters = {"c", "o", "b", "l"}
    initial = word[0].lower()
    ending = word[-1].lower()
    return initial in letters or ending in letters
