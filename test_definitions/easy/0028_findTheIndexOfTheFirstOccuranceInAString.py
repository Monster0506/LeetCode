from typing import List, Dict, Any, Tuple

METHOD_NAME = "strStr"

TEST_CASES: List[Dict[str, Any]] = [
    {
        "name": "Example 1: Basic occurrence at start",
        "args": ("sadbutsad", "sad"),
        "expected": 0,
    },
    {
        "name": "Example 2: No occurrence",
        "args": ("leetcode", "leeto"),
        "expected": -1,
    },
    {
        "name": "Needle at the beginning of haystack",
        "args": ("hello", "he"),
        "expected": 0,
    },
    {
        "name": "Needle at the end of haystack",
        "args": ("programming", "ing"),
        "expected": 8,
    },
    {
        "name": "Needle in the middle of haystack",
        "args": ("abcdefgh", "cde"),
        "expected": 2,
    },
    {
        "name": "Needle is same as haystack",
        "args": ("abc", "abc"),
        "expected": 0,
    },
    {
        "name": "Needle is longer than haystack",
        "args": ("short", "verylongneedle"),
        "expected": -1,
    },
    {
        "name": "Needle is empty string (standard behavior: returns 0)",
        "args": ("abc", ""),
        "expected": 0,
    },
    {
        "name": "Haystack is empty string, needle is non-empty",
        "args": ("", "a"),
        "expected": -1,
    },
    {
        "name": "Both haystack and needle are empty strings",
        "args": ("", ""),
        "expected": 0,
    },
    {
        "name": "Needle occurs multiple times, return first",
        "args": ("ababab", "aba"),
        "expected": 0,
    },
    {
        "name": "Needle with repeated characters, no match",
        "args": ("aaaaa", "bba"),
        "expected": -1,
    },
    {
        "name": "Needle with repeated characters, match",
        "args": ("aaaaa", "aaa"),
        "expected": 0,
    },
    {
        "name": "Needle is single character, multiple occurrences",
        "args": ("mississippi", "i"),
        "expected": 1,
    },
    {
        "name": "Needle is single character, no occurrence",
        "args": ("abcde", "f"),
        "expected": -1,
    },
    {
        "name": "Long haystack, short needle at beginning",
        "args": ("abcdefghijklmnopqrstuvwxyz", "abc"),
        "expected": 0,
    },
    {
        "name": "Long haystack, short needle at end",
        "args": ("abcdefghijklmnopqrstuvwxyz", "xyz"),
        "expected": 23,
    },
    {
        "name": "Long haystack, short needle in middle",
        "args": ("abcdefghijklmnopqrstuvwxyz", "mno"),
        "expected": 12,
    },
    {
        "name": "Needle matches last character of haystack",
        "args": ("abcde", "e"),
        "expected": 4,
    },
    {
        "name": "Haystack with single character, needle matches",
        "args": ("a", "a"),
        "expected": 0,
    },
    {
        "name": "Haystack with single character, needle no match",
        "args": ("a", "b"),
        "expected": -1,
    },
    {
        "name": "Needle slightly longer than remaining haystack",
        "args": ("abc", "abcd"),
        "expected": -1,
    },
    {
        "name": "Edge case: haystack just barely contains needle at end",
        "args": ("aaaaab", "ab"),
        "expected": 4,
    },
    {
        "name": "Complex overlapping pattern, first match",
        "args": ("aaaaaaaab", "aaab"),
        "expected": 5,
    },
    {
        "name": "Long string with no match",
        "args": (
            "antidisestablishmentarianism",
            "pneumonoultramicroscopicsilicovolcanoconiosis",
        ),
        "expected": -1,
    },
    {
        "name": "Large identical strings (up to constraint limit)",
        "args": ("a" * 100, "a" * 100),
        "expected": 0,
    },
    {
        "name": "Large haystack, small needle at end",
        "args": ("a" * 9999 + "b", "b"),
        "expected": 9999,
    },
    {
        "name": "Large haystack, small needle at beginning",
        "args": ("b" + "a" * 9999, "b"),
        "expected": 0,
    },
]

# DEFAULT_TIMEOUT is optional
# DEFAULT_TIMEOUT = 1.0 # Could set a default timeout if needed
