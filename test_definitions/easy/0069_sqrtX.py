from typing import List, Dict, Any

# METHOD_NAME is required
METHOD_NAME = "mySqrt"

# TEST_CASES is required
TEST_CASES: List[Dict[str, Any]] = [
    {"name": "Example 1: Perfect square", "args": (4,), "expected": 2},  # x = 4
    {
        "name": "Example 2: Non-perfect square, rounds down",
        "args": (8,),
        "expected": 2,
    },
    {"name": "Smallest case: x = 0", "args": (0,), "expected": 0},
    {"name": "Smallest non-zero case: x = 1", "args": (1,), "expected": 1},
    {
        "name": "Non-perfect square: x = 2",
        "args": (2,),
        "expected": 1,
    },
    {
        "name": "Non-perfect square: x = 3",
        "args": (3,),
        "expected": 1,
    },
    {"name": "Medium perfect square", "args": (25,), "expected": 5},
    {
        "name": "Medium non-perfect square",
        "args": (26,),
        "expected": 5,
    },
    {
        "name": "Large perfect square (e.g., 65536 = 256*256)",
        "args": (65536,),
        "expected": 256,
    },
    {
        "name": "Large non-perfect square (just below max int)",
        "args": (2147395600,),
        "expected": 46340,
    },
    {
        "name": "Largest possible input: 2^31 - 1",
        "args": (2147483647,),
        "expected": 46340,
    },
    {
        "name": "Another non-perfect square, 99",
        "args": (99,),
        "expected": 9,
    },
    {"name": "Value requiring no change", "args": (100,), "expected": 10},
]

# DEFAULT_TIMEOUT = 1.0
