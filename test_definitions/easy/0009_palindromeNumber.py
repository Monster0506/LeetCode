from typing import List, Dict, Any  # For type hinting test cases

# The exact name of the method to test in the Solution class
METHOD_NAME = "isPalindrome"

# The list of test cases for this problem
TEST_CASES: List[Dict[str, Any]] = [
    {
        "name": "LeetCode Example 1: Positive Palindrome",
        "args": (121,),  # (x,)
        "expected": True,
    },
    {
        "name": "LeetCode Example 2: Negative Number",
        "args": (-121,),  # (x,)
        "expected": False,  # Negative numbers are not palindromes.
    },
    {
        "name": "LeetCode Example 3: Ends with 0 (not 0 itself)",
        "args": (10,),  # (x,)
        "expected": False,  # Reads 01 from right. Not a palindrome.
    },
    {
        "name": "Single Digit Zero",
        "args": (0,),  # (x,)
        "expected": True,
    },
    {
        "name": "Single Digit Positive",
        "args": (7,),  # (x,)
        "expected": True,
    },
    {
        "name": "Positive Non-Palindrome",
        "args": (123,),  # (x,)
        "expected": False,
    },
    {
        "name": "Even Length Palindrome",
        "args": (1221,),  # (x,)
        "expected": True,
    },
    {
        "name": "Even Length Non-Palindrome",
        "args": (1231,),  # (x,)
        "expected": False,
    },
    {
        "name": "Number ending in 0, multi-digit, not palindrome",
        "args": (100,),  # (x,)
        "expected": False,  # Reversed: 001. Not a palindrome.
    },
    {
        "name": "Large Palindrome",
        "args": (123454321,),  # (x,)
        "expected": True,
    },
    {
        "name": "Large Non-Palindrome",
        "args": (123456789,),  # (x,)
        "expected": False,
    },
    {
        "name": "Palindrome with internal zeros",
        "args": (10001,),  # (x,)
        "expected": True,
    },
    {
        "name": "Non-palindrome ending in zero with internal zeros",
        "args": (10010,),  # (x,)
        "expected": False,  # Reversed: 01001. Not a palindrome.
    },
    {
        "name": "Max 32-bit signed int (non-palindrome)",
        "args": (2147483647,),  # (x,)
        "expected": False,
    },
    {
        "name": "Large palindrome near max 32-bit int",
        "args": (2147447412,),  # (x,)
        "expected": True,
    },
    {
        "name": "Large non-palindrome near max 32-bit int",
        "args": (2147483646,),  # (x,)
        "expected": False,
    },
    {
        "name": "Smallest multi-digit palindrome",
        "args": (11,),  # (x,)
        "expected": True,
    },
]

# Optional: You can also define a default timeout for this specific problem's tests
# DEFAULT_TIMEOUT = 1.0  # seconds
