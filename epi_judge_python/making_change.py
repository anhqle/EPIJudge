from test_framework import generic_test


def change_making(cents: int) -> int:
    coins = [1, 5, 10, 25, 50, 100]
    num_coins = 0
    for coin in coins[::-1]:
        num_coins += cents // coin 
        cents = cents % coin
    return num_coins


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('making_change.py', 'making_change.tsv',
                                       change_making))
