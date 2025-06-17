from typing import List, Dict, Any, Tuple

# METHOD_NAME is required
METHOD_NAME = "lengthOfLastWord"

# TEST_CASES is required
TEST_CASES: List[Dict[str, Any]] = [
    {
        "name": "Example 1: Basic case with two words",
        "args": ("Hello World",),
        "expected": 5,
    },
    {
        "name": "Example 2: Multiple leading/trailing/inter-word spaces",
        "args": ("   fly me   to   the moon  ",),
        "expected": 4,
    },
    {
        "name": "Example 3: Simple sentence",
        "args": ("luffy is still joyboy",),
        "expected": 6,
    },
    {
        "name": "Single word, no spaces",
        "args": ("word",),
        "expected": 4,
    },
    {
        "name": "Single word with trailing spaces",
        "args": ("apple   ",),
        "expected": 5,
    },
    {
        "name": "Single word with leading spaces",
        "args": ("   banana",),
        "expected": 6,
    },
    {
        "name": "Single word with leading and trailing spaces",
        "args": ("   cherry   ",),
        "expected": 6,
    },
    {
        "name": "String with multiple words and a single trailing space",
        "args": ("hello world ",),
        "expected": 5,
    },
    {
        "name": "String with multiple words and multiple trailing spaces",
        "args": ("test string   ",),
        "expected": 6,
    },
    {
        "name": "String with multiple words and a single leading space",
        "args": (" one two three",),
        "expected": 5,
    },
    {
        "name": "String with multiple words and multiple leading spaces",
        "args": ("   four five six",),
        "expected": 3,
    },
    {
        "name": "String with a very long last word",
        "args": ("a " + "b" * 100 + "c",),
        "expected": 101,
    },
    {
        "name": "String with mixed case words",
        "args": ("First Second THIRD",),
        "expected": 5,
    },
    {
        "name": "String with single character last word",
        "args": ("a b c",),
        "expected": 1,
    },
    {
        "name": ("String ending with a single character and trailing spaces"),
        "args": ("wordz x y z   ",),
        "expected": 1,
    },
    {
        "name": "All words are single characters",
        "args": ("a b c d e f g",),
        "expected": 1,
    },
    {
        "name": "String with no spaces, single word",
        "args": ("ProgrammingIsFun",),
        "expected": 16,
    },
    {
        "name": "String with many spaces between words",
        "args": ("This    is     a     test",),
        "expected": 4,
    },
    {
        "name": "String with alternating words and spaces",
        "args": ("a b c d e",),
        "expected": 1,
    },
    {
        "name": "Max length string, single word",
        "args": ("x" * 10000,),
        "expected": 10000,
    },
    {
        "name": "Max length string, last word is short",
        "args": ("a" * 9995 + " last",),
        "expected": 4,
    },
    {
        "name": "Max length string, with many spaces",
        "args": ("a " * 5000 + "final_word",),
        "expected": 10,
    },
    {
        "name": "Another sentence with typical spacing",
        "args": ("The quick brown fox jumps over the lazy dog",),
        "expected": 3,
    },
]
