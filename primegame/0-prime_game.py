#!/usr/bin/python3
"""Prime Game module."""


def isWinner(x, nums):
    """
    Determine who wins the most rounds of the Prime Game.

    Maria and Ben play x rounds. In each round, starting from a set of
    consecutive integers 1 to n, they alternately pick a prime number
    still in the set and remove it and all its multiples. Maria goes
    first. The player unable to move loses that round.

    Args:
        x (int): number of rounds.
        nums (list): list of n values, one per round.

    Returns:
        str: name of the player with the most wins ("Maria" or "Ben"),
             or None if there is a tie or invalid input.
    """
    if x is None or nums is None or x < 1 or len(nums) < 1:
        return None

    n = max(nums)
    if n < 2:
        # No primes at all in any round below 2; Ben always wins these.
        sieve = []
    else:
        sieve = [True] * (n + 1)
        sieve[0] = sieve[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if sieve[i]:
                for multiple in range(i * i, n + 1, i):
                    sieve[multiple] = False

    # prime_count[i] = number of primes <= i
    prime_count = [0] * (n + 1) if n >= 0 else []
    for i in range(2, n + 1):
        prime_count[i] = prime_count[i - 1] + (1 if sieve[i] else 0)

    maria_wins = 0
    ben_wins = 0

    for round_n in nums:
        if round_n < 2:
            count = 0
        else:
            count = prime_count[round_n]

        if count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    if ben_wins > maria_wins:
        return "Ben"
    return None
