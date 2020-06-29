from typing import List

from test_framework import generic_test, test_utils


def phone_mnemonic(phone_number: str) -> List[str]:

    mapping = {'1': ['1'], '2': ['A', 'B', 'C'], '3': ['D', 'E', 'F'], '4': ['G', 'H', 'I'],
             '5': ['J', 'K', 'L'], '6': ['M', 'N', 'O'], '7': ['P', 'Q', 'R', 'S'], 
             '8': ['T', 'U', 'V'], '9': ['W', 'X', 'Y', 'Z'], '0': ['0']}
    res = []
    A = [c for c in phone_number]
    def util(i):
        if i == len(A):
            res.append(''.join(A))
            return
        for char in mapping[phone_number[i]]:
            A[i] = char
            util(i + 1)
            
    util(0)
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'phone_number_mnemonic.py',
            'phone_number_mnemonic.tsv',
            phone_mnemonic,
            comparator=test_utils.unordered_compare))
