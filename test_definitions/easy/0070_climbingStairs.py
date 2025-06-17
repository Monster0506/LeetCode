from typing import (
    List,
    Dict,
    Any,
    Tuple,  # Still good to include even if not directly used in args
    Optional,
)

METHOD_NAME = "climbStairs"

TEST_CASES: List[Dict[str, Any]] = [
    {"name": "Example 1: n = 2", "args": (2,), "expected": 2},
    {"name": "Example 2: n = 3", "args": (3,), "expected": 3},
    {
        "name": "Smallest valid input: n = 1",
        "args": (1,),
        "expected": 1,
    },
    {
        "name": "n = 4",
        "args": (4,),
        "expected": 5,
    },
    {
        "name": "n = 5",
        "args": (5,),
        "expected": 8,
    },
    {"name": "n = 6", "args": (6,), "expected": 13},
    {"name": "n = 7", "args": (7,), "expected": 21},
    {"name": "n = 8", "args": (8,), "expected": 34},
    {"name": "n = 9", "args": (9,), "expected": 55},
    {"name": "n = 10", "args": (10,), "expected": 89},
    {"name": "n = 15", "args": (15,), "expected": 987},
    {"name": "n = 20", "args": (20,), "expected": 10946},
    {"name": "n = 25", "args": (25,), "expected": 121393},
    {"name": "n = 30", "args": (30,), "expected": 1346269},
    {"name": "n = 35", "args": (35,), "expected": 14930352},
    {"name": "n = 40", "args": (40,), "expected": 165580141},
    {
        "name": "n = 45 (Common max for this type, F(45))",
        "args": (45,),
        "expected": 1836311903,
    },
]

# DEFAULT_TIMEOUT is optional.
# DEFAULT_TIMEOUT = 1.0
