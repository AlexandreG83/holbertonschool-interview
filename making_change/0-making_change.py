#!/usr/bin/python3
"""
Module for calculating the fewest number of coins needed to meet a given total.
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.

    Args:
        coins (list): List of coin denominations (integers > 0).
        total (int): The target total amount.

    Returns:
        int: Fewest number of coins needed to meet total.
             Returns 0 if total is 0 or less.
             Returns -1 if total cannot be met by any combination.
    """
    if total <= 0:
        return 0

    # Initialize dp array with a value larger than any possible solution
    INF = total + 1
    dp = [INF] * (total + 1)
    dp[0] = 0

    for amount in range(1, total + 1):
        for coin in coins:
            if coin <= amount:
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    if dp[total] != INF:
        return dp[total]
    else:
        return -1
