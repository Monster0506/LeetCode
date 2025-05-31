from typing import List, Dict, Any  # For type hinting test cases

# The exact name of the method to test in the Solution class
METHOD_NAME = "isValid"

# The list of test cases for this problem
TEST_CASES: List[Dict[str, Any]] = [
    {
        "name": "LeetCode Example 1: Simple Parentheses",
        "args": ("()",),  # (s,)
        "expected": True,
    },
    {
        "name": "LeetCode Example 2: All Types Valid",
        "args": ("()[]{}",),  # (s,)
        "expected": True,
    },
    {
        "name": "LeetCode Example 3: Mismatched Pair",
        "args": ("(]",),  # (s,)
        "expected": False,
    },
    {
        "name": "Empty String",
        "args": ("",),  # (s,)
        "expected": True,  # No brackets to be invalid
    },
    {
        "name": "Simple Brackets Valid",
        "args": ("[]",),
        "expected": True,
    },
    {
        "name": "Simple Braces Valid",
        "args": ("{}",),
        "expected": True,
    },
    {
        "name": "Nested Valid: Parentheses",
        "args": ("(())",),
        "expected": True,
    },
    {
        "name": "Nested Valid: Mixed",
        "args": ("{[]}",),
        "expected": True,
    },
    {
        "name": "Nested Valid: Complex",
        "args": ("([{}])",),
        "expected": True,
    },
    {
        "name": "Invalid: Incorrect Order",
        "args": ("([)]",),
        "expected": False,
    },
    {
        "name": "Invalid: Unclosed Opening Bracket",
        "args": ("{[](",),
        "expected": False,
    },
    {
        "name": "Invalid: Closing Bracket Without Opening",
        "args": ("]",),
        "expected": False,
    },
    {
        "name": "Invalid: Opening Bracket Without Closing",
        "args": ("(",),
        "expected": False,
    },
    {
        "name": "Invalid: Too Many Closing Brackets",
        "args": ("())",),
        "expected": False,
    },
    {
        "name": "Invalid: Mismatched Nested",
        "args": ("{[}]",),
        "expected": False,
    },
    {
        "name": "Invalid: Starts with Closing",
        "args": (")(",),
        "expected": False,
    },
    {
        "name": "Valid: Long Sequence",
        "args": ("(((((())))))",),
        "expected": True,
    },
    {
        "name": "Invalid: Long Sequence Unbalanced",
        "args": ("((((((())))))",),  # Extra opening
        "expected": False,
    },
    {
        "name": "Invalid: Long Sequence Unbalanced 2",
        "args": ("(((((()))))))",),  # Extra closing
        "expected": False,
    },
    {
        "name": "Valid: Complex Nested Structure",
        "args": ("([]{[]})",),
        "expected": True,
    },
    {
        "name": "Invalid: Complex Mismatched Nested",
        "args": ("([]{[}])",),
        "expected": False,
    },
    {
        "name": "Only Opening Brackets",
        "args": ("(((",),
        "expected": False,
    },
    {
        "name": "Only Closing Brackets",
        "args": ("]]]",),
        "expected": False,
    },
    {
        "name": "Valid: Multiple Sequential Pairs",
        "args": ("()()()",),
        "expected": True,
    },
    {
        "name": "Valid: Mixed Sequential and Nested",
        "args": ("({})[({})]",),
        "expected": True,
    },
    {
        "name": "Invalid: Mismatched Closing for Outer",
        "args": ("({)}",),
        "expected": False,
    },
    {
        "name": "Invalid: Unclosed Inner Bracket",
        "args": ("([)",),
        "expected": False,
    },
    {
        "name": "Valid: Deeply Nested Single Type",
        "args": ("[[[[]]]]",),
        "expected": True,
    },
    {
        "name": "Invalid: Deeply Nested Single Type Unclosed",
        "args": ("[[[[]]",),
        "expected": False,
    },
]

# Optional: You can also define a default timeout for this specific problem's tests
# DEFAULT_TIMEOUT = 1.0  # seconds
