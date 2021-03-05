# kata: https://www.codewars.com/kata/56747fd5cb988479af000028

def get_middle(s: str):
    mid: int = len(s) // 2
    return (
        s[mid - 1:mid + 1]
        if is_even(len(s))
        else s[mid:mid+1]
    )


def is_even(num: int) -> bool:
    return int(num) % 2 == 0


assert get_middle("test") == "es", "Assert"
assert get_middle("testing") == "t", "Assert"
assert get_middle("middle") == "dd", "Assert"
assert get_middle("A") == "A", "Assert"
assert get_middle("of") == "of", "Assert"
