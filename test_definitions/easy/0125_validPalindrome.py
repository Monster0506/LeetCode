from typing import List, Dict, Any

# METHOD_NAME is required
METHOD_NAME = "isPalindrome"

# TEST_CASES is required
TEST_CASES: List[Dict[str, Any]] = [
    {
        "name": "Example 1: Classic palindrome",
        "args": ("A man, a plan, a canal: Panama",),
        "expected": True,
    },
    {
        "name": "Example 2: Not a palindrome",
        "args": ("race a car",),
        "expected": False,
    },
    {
        "name": "Example 3: Empty string after cleanup",
        "args": (" ",),
        "expected": True,
    },
    {
        "name": "Empty string",
        "args": ("",),
        "expected": True,
    },
    {
        "name": "Single alphanumeric character",
        "args": ("a",),
        "expected": True,
    },
    {
        "name": "Single non-alphanumeric character",
        "args": (".",),
        "expected": True,
    },
    {
        "name": "Only non-alphanumeric characters",
        "args": ("!@#$%^&*",),
        "expected": True,
    },
    {
        "name": "Simple palindrome (all lowercase, no spaces)",
        "args": ("madam",),
        "expected": True,
    },
    {
        "name": "Simple non-palindrome (all lowercase, no spaces)",
        "args": ("hello",),
        "expected": False,
    },
    {
        "name": "Palindrome with mixed case",
        "args": ("RaceCar",),
        "expected": True,
    },
    {
        "name": "Palindrome with numbers",
        "args": ("A1B22B1A",),
        "expected": True,
    },
    {
        "name": "Palindrome with mixed case",
        "args": ("Was it a car or a cat I saw?",),
        "expected": True,  # "wasitacaroracataisaw" is false
    },
    {
        "name": "Numbers only palindrome",
        "args": ("12321",),
        "expected": True,
    },
    {
        "name": "Numbers only non-palindrome",
        "args": ("12345",),
        "expected": False,
    },
    {
        "name": "Another long non-palindrome",
        "args": ("This is not a palindrome.",),  # "thisisnotapalindrome"
        "expected": False,
    },
    {
        "name": "String with only spaces",
        "args": ("   ",),
        "expected": True,
    },
    {
        "name": "String with leading/trailing spaces and punctuation",
        "args": ("  . ,,, Madam ,,.  ",),
        "expected": True,
    },
    {
        "name": "Palindrome with punctuation at start/end",
        "args": ("@level@",),
        "expected": True,
    },
    {
        "name": "Single letter with surrounding non-alphanumeric",
        "args": ("!a!",),
        "expected": True,
    },
    {
        "name": "Two different alphanumeric characters, no others",
        "args": ("ab",),
        "expected": False,
    },
    {
        "name": "Two same alphanumeric characters, no others",
        "args": ("aa",),
        "expected": True,
    },
    {
        "name": "Two different alphanumeric characters, separated by non-alphanumeric",
        "args": ("a,b",),
        "expected": False,
    },
    {
        "name": "Two same alphanumeric characters, separated by non-alphanumeric",
        "args": ("a.a",),
        "expected": True,
    },
    {
        "name": "Palindrome with 0 and P",
        "args": ("0P",),  # Becomes "0p", which is not a palindrome.
        "expected": False,
    },
    {
        "name": "Palindrome with mixed numbers and letters and symbols",
        "args": ("Ab-a-",),  # "aba"
        "expected": True,
    },
    {
        "name": "Non-palindrome with numbers and special chars",
        "args": ("_123*321@",),  # "123321" - this IS a palindrome
        "expected": True,
    },
    {
        "name": "Almost palindrome, single character difference in middle",
        "args": ("levela",),  # "levela" is not a palindrome
        "expected": False,
    },
    {
        "name": "Long string, all alphanumeric, true",
        "args": ("qwertyuiopasdfghjklzxcvbnmmnbvcxzlkjhgfdsapoiuYtrewq",),
        "expected": True,
    },
    {
        "name": "Long string, all alphanumeric, false",
        "args": ("abcdefghijklmnopqrstuvwxyzzyxwuvtsrqponmlkjihgfedcba",),
        "expected": False,
    },
    {
        "name": "String with only numeric characters and spaces",
        "args": ("1 2 3 2 1",),  # "12321"
        "expected": True,
    },
    {
        "name": "String with only numeric characters and symbols",
        "args": ("!123@432#1$",),  # "1234321"
        "expected": True,
    },
    {
        "name": "String with only one repeating alphanumeric character and noise",
        "args": ("...aaa...",),  # "aaa"
        "expected": True,
    },
    {
        "name": "String with odd length, palindrome",
        "args": ("Madam, I'm Adam.",),  # "madamimadam"
        "expected": True,
    },
    {
        "name": "String with even length, palindrome",
        "args": ("No Lemon, No Melon.",),  # "nolemonnomelon"
        "expected": True,
    },
    {
        "name": "String with leading zeros (as numbers)",
        "args": ("007racecar700",),  # "007racecar700"
        "expected": True,
    },
    {
        "name": "String with mixed numbers/letters and mixed case, palindrome",
        "args": ("_aBccBa_",),  # "abccba"
        "expected": True,
    },
    {
        "name": "String with mixed numbers/letters and mixed case, not palindrome",
        "args": ("_aB1cBb_",),  # "ab1cbb"
        "expected": False,
    },
]

# DEFAULT_TIMEOUT is optional. String operations are usually fast enough for typical constraints.
# DEFAULT_TIMEOUT = 1.0
