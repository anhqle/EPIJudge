from test_framework import generic_test
from test_framework.test_failure import TestFailure
import collections


class Stack:
    class MaxWithCount:
        def __init__(self, value, count):
            self.value, self.count = value, count

    def __init__(self):
        self.data = []
        self.max_stack = []

    def empty(self) -> bool:
        return len(self.data) == 0

    def max(self) -> int:
        if self.max_stack:
            return self.max_stack[-1].value
        raise Exception

    def pop(self) -> int:
        if not self.empty():
            item = self.data.pop()
            if item == self.max():
                if self.max_stack[-1].count > 1:
                    self.max_stack[-1].count -= 1
                else:
                    self.max_stack.pop()
            return item
        raise Exception

    def push(self, x: int) -> None:
        # Push
        self.data.append(x)

        # Update max
        if self.max_stack:
            if x > self.max():
                self.max_stack.append(self.MaxWithCount(x, 1))
            elif x == self.max():
                self.max_stack[-1].count += 1
        else:
            self.max_stack.append(self.MaxWithCount(x, 1))


def stack_tester(ops):
    try:
        s = Stack()

        for (op, arg) in ops:
            if op == 'Stack':
                s = Stack()
            elif op == 'push':
                s.push(arg)
            elif op == 'pop':
                result = s.pop()
                if result != arg:
                    raise TestFailure('Pop: expected ' + str(arg) + ', got ' +
                                      str(result))
            elif op == 'max':
                result = s.max()
                if result != arg:
                    raise TestFailure('Max: expected ' + str(arg) + ', got ' +
                                      str(result))
            elif op == 'empty':
                result = int(s.empty())
                if result != arg:
                    raise TestFailure('Empty: expected ' + str(arg) +
                                      ', got ' + str(result))
            else:
                raise RuntimeError('Unsupported stack operation: ' + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('stack_with_max.py',
                                       'stack_with_max.tsv', stack_tester))
