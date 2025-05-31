from typing import List, Dict, Any  # For type hinting test cases

# The exact name of the method to test in the Solution class
METHOD_NAME = "twoSum"

# The list of test cases for this problem
TEST_CASES: List[Dict[str, Any]] = [
    {
        "name": "Example 1",
        "args": ([2, 7, 11, 15], 9),  # (nums, target)
        "expected": [0, 1],
    },
    {"name": "Example 2", "args": ([3, 2, 4], 6), "expected": [1, 2]},
    {"name": "Example 3", "args": ([3, 3], 6), "expected": [0, 1]},
    {"name": "No solution", "args": ([1, 2, 3], 7), "expected": []},
    {"name": "Empty list", "args": ([], 5), "expected": []},
]

# Optional: You can also define a default timeout for this specific problem's tests
# DEFAULT_TIMEOUT = 1.0  # seconds
