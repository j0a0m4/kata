from uri_1069 import solution

SCENARIOS_FILE = "uri_1069_scenarios.txt"


def assert_is_equal(example, expected):
    actual = solution(example)

    display = f"""
    \t Case: solution(\"{example}\")
    \t Expected: {expected}
    \t Actual: {actual}"""

    assert actual == expected, f"FAIL! {display}"
    print(f"PASSED! {display}")


with open(SCENARIOS_FILE, 'r') as reader:
    for line in reader:
        example, expected = tuple(line.strip().split(","))
        assert_is_equal(example, int(expected))
