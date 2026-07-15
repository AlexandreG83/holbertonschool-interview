Prime Game

Description

Solution to the Holberton "Prime Game" interview project.

Maria and Ben play x rounds of a game. In each round, starting from
the set of consecutive integers 1 to n, players alternately pick a
prime number still present in the set and remove it along with all its
multiples. Maria always goes first; whoever cannot pick a prime loses
that round.

Key insight

A prime number can only ever be removed by being picked directly - it
can never be removed as a multiple of a smaller prime, since a prime
has no smaller prime factors. This means the number of moves in a
round is always exactly the number of primes <= n, regardless of the
order in which players pick. So the winner of a round depends only on
the parity of that count:


odd count -> Maria (first player) makes the last move -> Maria wins
even count (including 0) -> Ben wins


Files


0-prime_game.py: contains isWinner(x, nums), which computes, for
each round, the number of primes up to n using a single sieve of
Eratosthenes built up to max(nums), then tallies wins and returns
the name of the player who won the most rounds (or None on a tie
or invalid input).


Requirements


Ubuntu 14.04 LTS, python3 (3.4.3)
PEP 8 (pycodestyle 1.7.x) style
No imports allowed in this task
Files start with #!/usr/bin/python3 and are executable