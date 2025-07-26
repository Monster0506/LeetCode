from typing import Any, Dict, List, Tuple


# METHOD_NAME is required
METHOD_NAME = "isAnagram"

# TEST_CASES is required
TEST_CASES: List[Dict[str, Any]] = [
    {
        "name": "Example 1: Basic anagram",
        "args": ("anagram", "nagaram"),
        "expected": True,
    },
    {
        "name": "Example 2: Different characters",
        "args": ("rat", "car"),
        "expected": False,
    },
    {
        "name": "Different lengths (s longer)",
        "args": ("hello", "hell"),
        "expected": False,
    },
    {
        "name": "Different lengths (t longer)",
        "args": ("cat", "cats"),
        "expected": False,
    },
    {
        "name": "Single character, anagram",
        "args": ("a", "a"),
        "expected": True,
    },
    {
        "name": "Single character, not anagram",
        "args": ("a", "b"),
        "expected": False,
    },
    {
        "name": "All same characters, anagram",
        "args": ("aaaaa", "aaaaa"),
        "expected": True,
    },
    {
        "name": "All same characters, not anagram (different counts)",
        "args": ("aaaa", "aaa"),
        "expected": False,
    },
    {
        "name": "Strings with unique characters, anagram",
        "args": ("abc", "bca"),
        "expected": True,
    },
    {
        "name": "Strings with unique characters, not anagram",
        "args": ("abc", "abd"),
        "expected": False,
    },
    {
        "name": "Strings with mixed character frequencies, anagram",
        "args": ("aabbc", "abcab"),
        "expected": True,
    },
    {
        "name": "Strings with mixed character frequencies, not anagram (missing char)",
        "args": ("aabbc", "aabdd"),
        "expected": False,
    },
    {
        "name": "Strings with mixed character frequencies, not anagram (different counts)",
        "args": ("aabbc", "aaabb"),
        "expected": False,
    },
    {
        "name": "Long strings, anagram",
        "args": (
            "abcdefghijklmnopqrstuvwxyz" * 1000,
            "zyxwuvtsrqponmlkjihgfedcba" * 1000,
        ),
        "expected": True,
    },
    {
        "name": "Long strings, not anagram (one character difference)",
        "args": (
            "abcdefghijklmnopqrstuvwxyza" * 1000,
            "zyxwuvtsrqponmlkjihgfedcba" * 1000,
        ),
        "expected": False,
    },
    {
        "name": "Long strings, not anagram (length difference)",
        "args": (
            "abcdefghijklmnopqrstuvwxyz" * 1000,
            "zyxwuvtsrqponmlkjihgfedcba" * 999,
        ),
        "expected": False,
    },
    {
        "name": "Strings with all characters present",
        "args": ("abcdefghijklmnopqrstuvwxyz", "abcdefghijklmnopqrstuvwxyz"[::-1]),
        "expected": True,
    },
]

# DEFAULT_TIMEOUT is optional. Constraints are generous.
# DEFAULT_TIMEOUT = 1.0
