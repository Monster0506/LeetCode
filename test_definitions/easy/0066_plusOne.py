from typing import List, Dict, Any, Tuple

# METHOD_NAME is required
METHOD_NAME = "plusOne"

# TEST_CASES is required
TEST_CASES: List[Dict[str, Any]] = [
    {
        "name": "Example 1: Basic increment, no carry",
        "args": ([1, 2, 3],),
        "expected": [1, 2, 4],
    },
    {
        "name": "Example 2: Basic increment, no carry (different digits)",
        "args": ([4, 3, 2, 1],),
        "expected": [4, 3, 2, 2],
    },
    {
        "name": "Example 3: Single digit, carry creates new digit",
        "args": ([9],),
        "expected": [1, 0],
    },
    {
        "name": "All nines, multiple digits (carry propagates)",
        "args": ([9, 9],),
        "expected": [1, 0, 0],
    },
    {
        "name": "All nines, many digits (carry propagates fully)",
        "args": ([9, 9, 9, 9],),
        "expected": [1, 0, 0, 0, 0],
    },
    {
        "name": "Last digit is 0, no carry",
        "args": ([1, 2, 0],),
        "expected": [1, 2, 1],
    },
    {
        "name": "Last digit is 8, no carry",
        "args": ([1, 2, 8],),
        "expected": [1, 2, 9],
    },
    {
        "name": "Mixed digits, carry stops in middle",
        "args": ([1, 2, 3, 9, 9],),
        "expected": [1, 2, 4, 0, 0],
    },
    {
        "name": "Mixed digits, carry stops at first digit",
        "args": ([8, 9, 9],),
        "expected": [9, 0, 0],
    },
    {
        "name": "Single digit, no carry",
        "args": ([5],),
        "expected": [6],
    },
    {
        "name": "Two digits, last is 9, carry",
        "args": ([1, 9],),
        "expected": [2, 0],
    },
    {
        "name": "Two digits, no carry",
        "args": ([2, 3],),
        "expected": [2, 4],
    },
    {
        "name": "Input is [0] (representing integer 0, a valid single digit)",
        "args": ([0],),
        "expected": [1],
    },
    {
        "name": "Long array, no carries (to test performance)",
        "args": ([1] * 100 + [2],),
        "expected": [1] * 100 + [3],
        "timeout": 0.2,
    },
    {
        "name": "Long array, full carries (to test performance)",
        "args": ([9] * 100,),
        "expected": [1] + [0] * 100,
        "timeout": 0.2,
    },
    {
        "name": "Long array",
        "args": ([1, 2, 3, 4, 5, 9, 9, 9, 1, 2, 3, 4, 5],),
        "expected": [1, 2, 3, 4, 5, 9, 9, 9, 1, 2, 3, 4, 6],
        "timeout": 0.2,
    },
    {
        "name": "Array of ones, no carry",
        "args": ([1, 1, 1],),
        "expected": [1, 1, 2],
    },
    {
        "name": "Array of zeros and ones, with carry",
        "args": ([1, 0, 9],),
        "expected": [1, 1, 0],
    },
    {
        "name": "Large number ending in multiple zeros, but not all nines",
        "args": ([1, 2, 3, 4, 5, 6, 7, 8, 9, 0],),
        "expected": [1, 2, 3, 4, 5, 6, 7, 8, 9, 1],
    },
    {
        "name": "Large number with first digit as 9, but not all nines",
        "args": ([9, 8, 7],),
        "expected": [9, 8, 8],
    },
    {
        "name": "Number with alternating 8s and 9s, ending in 9",
        "args": ([8, 9, 8, 9],),
        "expected": [8, 9, 9, 0],
    },
    {
        "name": "Number with alternating 8s and 9s, ending in 8",
        "args": ([8, 9, 8, 8],),
        "expected": [8, 9, 8, 9],
    },
    {
        "name": "Longest possible array of digits (10^4 length), all nines",
        "args": ([9] * 10000,),
        "expected": [1] + [0] * 10000,
        "timeout": 0.5,
    },
    {
        "name": "Longest possible array, only last digit needs increment",
        "args": ([1] * 9999 + [2],),
        "expected": [1] * 9999 + [3],
        "timeout": 0.5,
    },
    {
        "name": "Longest possible array, all 1s, plus one",
        "args": ([1] * 10000,),
        "expected": [1] * 9999 + [2],
        "timeout": 0.5,
    },
]
