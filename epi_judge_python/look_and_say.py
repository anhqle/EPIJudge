from test_framework import generic_test
from collections import namedtuple

class Item(object):
    def __init__(self, num, count):
        self.num = num
        self.count = count

def look_and_say(n: int) -> str:

    def next_sequence(seq: str) -> str:

        if len(seq) == 1:
            return '1' + seq[0]

        res = []
        cur = Item(seq[0], 1)
        for num in seq[1:]:
            if num != cur.num:
                res.append(cur)
                cur = Item(num, 1)
            else:
                cur.count += 1
        
        res.append(cur)
        return ''.join([str(item.count) + item.num for item in res])

    seq = '1'
    for i in range(n - 1):
        seq = next_sequence(seq)

    return seq




            

    return ''


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('look_and_say.py', 'look_and_say.tsv',
                                       look_and_say))
