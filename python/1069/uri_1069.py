# kata: https://www.urionlinejudge.com.br/judge/pt/problems/view/1069

def main():
    n = int(input())
    for _ in range(0, n):
        solution(mine=input())


def solution(mine: str) -> int:
    diamonds = mine.replace('.', '')
    return count_diamonds(diamonds)


def count_diamonds(diamonds: str, count: int = 0) -> int:
    index = diamonds.find('<>')
    if index == -1:
        return count
    else:
        leftovers = diamonds.replace('<>', '', 1)
        return count_diamonds(leftovers, count + 1)
