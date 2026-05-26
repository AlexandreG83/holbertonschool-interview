#!/usr/bin/env python3
"""
complexity: O(√n)

12 ÷ 2 → OK → +2
6 ÷ 2 → OK → +2
3 ÷ 3 → OK → +3
total = 7

factor → 1 Copy All and many Paste
"""


def minOperations(n):
    operations = 0
    factor = 2

    if n <= 1:
        return 0

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
