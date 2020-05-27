import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Assume s is a list of strings, each of which is of length 1, e.g.,
# ['r', 'a', 'm', ' ', 'i', 's', ' ', 'c', 'o', 's', 't', 'l', 'y'].
def reverse_words(s):

    def reverse(s):
        for i in range(len(s) // 2):
            s[i], s[-1 - i] = s[-1 - i], s[i]
        return s

    reverse(s)

    l = r = 0
    while r <= len(s):
        if r == len(s) or s[r] == ' ':
            s[l:r] = reverse(s[l:r])
            l = r + 1
        r += 1
    



@enable_executor_hook
def reverse_words_wrapper(executor, s):
    s_copy = list(s)

    executor.run(functools.partial(reverse_words, s_copy))

    return ''.join(s_copy)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_words.py', 'reverse_words.tsv',
                                       reverse_words_wrapper))
