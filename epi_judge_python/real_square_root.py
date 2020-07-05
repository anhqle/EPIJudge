from test_framework import generic_test
import math

def square_root(x: float) -> float:
    l, r = (x, 1.0) if x < 1.0 else (1.0, x)

    while not math.isclose(l, r):
        mid = (l + r) / 2
        mid_squared = mid * mid
        if mid_squared > x:
            r = mid
        else:
            l = mid
    
    return l
    

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('real_square_root.py',
                                       'real_square_root.tsv', square_root))
