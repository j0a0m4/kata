from uri_2728 import solution

SCENARIOS_FILE = "uri_2728_scenarios.txt"


def assert_is_equal(example, expected):
    actual = solution(example)
    display = f"solution(\"{example}\") == \"{expected}\""
    assert actual == expected, f"FAIL! \t {display}"
    print(f"PASSED! \t {display}")


with open(SCENARIOS_FILE, 'r') as reader:
    for line in reader:
        example, expected = tuple(line.strip().split(","))
        assert_is_equal(example, expected)
