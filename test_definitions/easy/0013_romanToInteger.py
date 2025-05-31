from typing import List, Dict, Any  # For type hinting test cases

# The exact name of the method to test in the Solution class
METHOD_NAME = "romanToInt"

# The list of test cases for this problem
TEST_CASES: List[Dict[str, Any]] = [
    {
        "name": "Example 1: Simple Addition (II)",
        "args": ("II",),  # (s,)
        "expected": 2,
    },
    {
        "name": "Example 2: Simple Addition (XII)",
        "args": ("XII",),  # (s,)
        "expected": 12,  # X + II = 10 + 2
    },
    {
        "name": "Example 3: Simple Addition (XXVII)",
        "args": ("XXVII",),  # (s,)
        "expected": 27,  # XX + V + II = 20 + 5 + 2
    },
    {
        "name": "Example 4: Subtraction (IV)",
        "args": ("IV",),  # (s,)
        "expected": 4,
    },
    {
        "name": "Example 5: Subtraction (IX)",
        "args": ("IX",),  # (s,)
        "expected": 9,
    },
    {
        "name": "Single Smallest Symbol",
        "args": ("I",),
        "expected": 1,
    },
    {
        "name": "Single Largest Symbol",
        "args": ("M",),
        "expected": 1000,
    },
    {
        "name": "All Symbols Additive",
        "args": ("MDCLXVI",),  # M+D+C+L+X+V+I = 1000+500+100+50+10+5+1
        "expected": 1666,
    },
    {
        "name": "LeetCode Example: LVIII",
        "args": ("LVIII",),  # L + V + III = 50 + 5 + 3
        "expected": 58,
    },
    {
        "name": "LeetCode Example: MCMXCIV",
        "args": ("MCMXCIV",),  # M + CM + XC + IV = 1000 + 900 + 90 + 4
        "expected": 1994,
    },
    {
        "name": "Subtraction XL",
        "args": ("XL",),
        "expected": 40,
    },
    {
        "name": "Subtraction XC",
        "args": ("XC",),
        "expected": 90,
    },
    {
        "name": "Subtraction CD",
        "args": ("CD",),
        "expected": 400,
    },
    {
        "name": "Subtraction CM",
        "args": ("CM",),
        "expected": 900,
    },
    {
        "name": "Multiple Subtractions: CDXLIV",
        "args": ("CDXLIV",),  # CD + XL + IV = 400 + 40 + 4
        "expected": 444,
    },
    {
        "name": "Multiple Subtractions: CMXCIX",
        "args": ("CMXCIX",),  # CM + XC + IX = 900 + 90 + 9
        "expected": 999,
    },
    {
        "name": "Max Standard Roman Numeral: MMMCMXCIX",
        "args": ("MMMCMXCIX",),  # 3000 + 900 + 90 + 9
        "expected": 3999,
    },
    {
        "name": "No Subtraction: III",
        "args": ("III",),
        "expected": 3,
    },
    {
        "name": "No Subtraction: XXX",
        "args": ("XXX",),
        "expected": 30,
    },
    {
        "name": "No Subtraction: CCC",
        "args": ("CCC",),
        "expected": 300,
    },
    {
        "name": "No Subtraction: MMM",
        "args": ("MMM",),
        "expected": 3000,
    },
    {
        "name": "Mixed: XIV",  # X + IV
        "args": ("XIV",),
        "expected": 14,
    },
    {
        "name": "Mixed: LXIX",  # L + X + IX
        "args": ("LXIX",),
        "expected": 69,
    },
    {
        "name": "Mixed: CMXL",  # CM + XL
        "args": ("CMXL",),
        "expected": 940,
    },
    {
        "name": "Current Year (2025)",
        "args": ("MMXXV",),  # M + M + X + X + V = 1000 + 1000 + 10 + 10 + 5
        "expected": 2025,
    },
]

# Optional: You can also define a default timeout for this specific problem's tests
# DEFAULT_TIMEOUT = 1.0  # seconds
