from typing import List, Dict, Any, Tuple

# METHOD_NAME is required
METHOD_NAME = "addBinary"

# TEST_CASES is required
TEST_CASES: List[Dict[str, Any]] = [
    {
        "name": "Example 1: Basic case with carry",
        "args": ("11", "1"),
        "expected": "100",
    },
    {
        "name": "Example 2: Longer strings, multiple carries",
        "args": ("1010", "1011"),
        "expected": "10101",
    },
    {
        "name": "Both single '0'",
        "args": ("0", "0"),
        "expected": "0",
    },
    {
        "name": "One '0', one '1'",
        "args": ("0", "1"),
        "expected": "1",
    },
    {
        "name": "One '1', one '0'",
        "args": ("1", "0"),
        "expected": "1",
    },
    {
        "name": "Both single '1'",
        "args": ("1", "1"),
        "expected": "10",
    },
    {
        "name": "Unequal lengths, shorter ends with 1, no carry propagation",
        "args": ("1000", "1"),
        "expected": "1001",
    },
    {
        "name": "Unequal lengths, shorter ends with 1, carry propagation",
        "args": ("1001", "11"),
        "expected": "1100",
    },
    {
        "name": "Unequal lengths, longer has leading 1s, shorter single one",
        "args": ("111", "1"),
        "expected": "1000",
    },
    {
        "name": "Unequal lengths, longer all ones, shorter single one",
        "args": ("1111", "1"),
        "expected": "10000",
    },
    {
        "name": "Strings of equal length, no carries",
        "args": ("101", "010"),
        "expected": "111",
    },
    {
        "name": "Strings of equal length, all carries",
        "args": ("111", "111"),
        "expected": "1110",
    },
    {
        "name": "Long strings, result length increases by 1",
        "args": ("1111111111", "1"),
        "expected": "10000000000",
    },
    {
        "name": "Long strings, both all ones, full carry propagation",
        "args": ("11111", "11111"),
        "expected": "111110",
    },
    {
        "name": "Long strings, alternating 1s and 0s, sum of 101010 + 101010",
        "args": ("101010", "101010"),
        "expected": "1010100",
    },
    {
        "name": "Very long strings, mostly zeros, some carries",
        "args": ("1" + "0" * 8 + "1", "1" + "0" * 8 + "1"),
        "expected": "10000000010",
        "timeout": 0.5,
    },
    {
        "name": "One string much shorter than other, last digits sum with carry",
        "args": ("1" * 22, "101"),
        "expected": "1" + "0" * 19 + "100",
        "timeout": 0.5,
    },
    {
        "name": "Sum of two long strings of all ones (equal length)",
        "args": ("1" * 51, "1" * 51),
        "expected": "1" + "1" * 50 + "0",
        "timeout": 0.5,
    },
    {
        "name": "String '0' and a long string",
        "args": ("0", "1" * 50),
        "expected": "1" * 50,
        "timeout": 0.2,
    },
    {
        "name": "Long string and '0'",
        "args": ("1010101010", "0"),
        "expected": "1010101010",
    },
    {
        "name": "Sum that results in only zeros (except first digit if there's a carry)",
        "args": ("101", "011"),
        "expected": "1000",
    },
    {
        "name": "Strings representing numbers with varying number of 1s",
        "args": ("1101", "101"),
        "expected": "10010",
    },
    {
        "name": "Many carries followed by no carries",
        "args": ("1111000", "0001"),
        "expected": "1111001",
    },
    {
        "name": "Edge case: 10 + 10",
        "args": ("10", "10"),
        "expected": "100",
    },
    {
        "name": "Edge case: 110 + 110",
        "args": ("110", "110"),
        "expected": "1100",
    },
    {
        "name": "Edge case: 1 + 100",
        "args": ("1", "100"),
        "expected": "101",
    },
]
