from typing import List

from test_framework import generic_test


# Given n, return all primes up to and including n.
def generate_primes(n: int) -> List[int]:
    is_prime = [True] * (n + 1)  # 0 to n
    is_prime[0:2] = [False, False]  # 0 and 1 is not a prime

    i = 2
    while i * 2 <= n:
        k = 2
        while i * k <= n:
            is_prime[i * k] = False
            k += 1
        i += 1

    return [i for i in range(len(is_prime)) if is_prime[i]]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('prime_sieve.py', 'prime_sieve.tsv',
                                       generate_primes))
