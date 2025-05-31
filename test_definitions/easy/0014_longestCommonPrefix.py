from typing import List, Dict, Any  # For type hinting test cases

# The exact name of the method to test in the Solution class
METHOD_NAME = "longestCommonPrefix"

# The list of test cases for this problem
TEST_CASES: List[Dict[str, Any]] = [
    {
        "name": "LeetCode Example 1",
        "args": (["flower", "flow", "flight"],),  # (strs,)
        "expected": "fl",
    },
    {
        "name": "LeetCode Example 2: No Common Prefix",
        "args": (["dog", "racecar", "car"],),  # (strs,)
        "expected": "",
    },
    {
        "name": "Empty List",
        "args": ([],),  # (strs,)
        "expected": "",
    },
    {
        "name": "List with One String",
        "args": (["apple"],),  # (strs,)
        "expected": "apple",
    },
    {
        "name": "List with One Empty String",
        "args": ([""],),  # (strs,)
        "expected": "",
    },
    {
        "name": "List with Multiple Empty Strings",
        "args": (["", "", ""],),  # (strs,)
        "expected": "",
    },
    {
        "name": "List with Empty String and Non-Empty Strings",
        "args": (["apple", "", "apricot"],),  # (strs,)
        "expected": "",
    },
    {
        "name": "List with Non-Empty String and Empty String at Start",
        "args": (["", "apple", "apricot"],),  # (strs,)
        "expected": "",
    },
    {
        "name": "All Strings are Identical",
        "args": (["leetcode", "leetcode", "leetcode"],),  # (strs,)
        "expected": "leetcode",
    },
    {
        "name": "Prefix is one of the strings",
        "args": (["prefix", "prefixextra", "prefixsuffix"],),  # (strs,)
        "expected": "prefix",
    },
    {
        "name": "Common Prefix of Length 1",
        "args": (["alpha", "apple", "apply"],),  # (strs,)
        "expected": "a",  # "ap" is not common to "alpha"
    },
    {
        "name": "Common Prefix of Length 2",
        "args": (["apple", "apricot", "application"],),  # (strs,)
        "expected": "ap",
    },
    {
        "name": "Strings of Different Lengths, Common Prefix",
        "args": (["ab", "abc", "abd"],),  # (strs,)
        "expected": "ab",
    },
    {
        "name": "Strings of Different Lengths, Common Prefix (shorter first)",
        "args": (["interstellar", "internet", "internal"],),  # (strs,)
        "expected": "inter",
    },
    {
        "name": "No Common Prefix, Different First Characters",
        "args": (["zebra", "yak", "xylophone"],),  # (strs,)
        "expected": "",
    },
    {
        "name": "Case Sensitivity: Common Prefix if Case Matched",
        "args": (["Flower", "Flow", "Flight"],),  # (strs,)
        "expected": "Fl",  # Assuming case-sensitive
    },
    {
        "name": "Case Sensitivity: No Common Prefix due to Case",
        "args": (["flower", "Flow", "flight"],),  # (strs,)
        "expected": "",
    },
    {
        "name": "Long Strings with Long Common Prefix",
        "args": (
            [
                "longcommonprefixstringexample",
                "longcommonprefixstringanother",
                "longcommonprefixstringyetanother",
            ],
        ),  # (strs,)
        "expected": "longcommonprefixstring",
    },
    {
        "name": "Long Strings with No Common Prefix",
        "args": (
            [
                "abcdefghijklmnopqrstuvwxyz",
                "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                "1234567890",
            ],
        ),  # (strs,)
        "expected": "",
    },
    {
        "name": "Prefix is the shortest string",
        "args": (["a", "ab", "abc"],),  # (strs,)
        "expected": "a",
    },
    {
        "name": "Prefix is the shortest string (reversed order)",
        "args": (["abc", "ab", "a"],),  # (strs,)
        "expected": "a",
    },
    {
        "name": "Two strings, one is prefix of other",
        "args": (["prefix", "prefixsuffix"],),  # (strs,)
        "expected": "prefix",
    },
    {
        "name": "Two strings, no common prefix",
        "args": (["hello", "world"],),  # (strs,)
        "expected": "",
    },
    {
        "name": "Two identical strings",
        "args": (["test", "test"],),  # (strs,)
        "expected": "test",
    },
]

# Optional: You can also define a default timeout for this specific problem's tests
# DEFAULT_TIMEOUT = 1.0  # seconds
