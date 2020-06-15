from typing import List

from test_framework import generic_test
from collections import namedtuple, deque

def flip_color(x: int, y: int, image: List[List[bool]]) -> None:
    Cell = namedtuple('Cell', ('x', 'y'))

    COLOR = image[x][y]
    q = deque([Cell(x, y)])
    while q:
        cur = q.popleft()
        if not (0 <= cur.x < len(image) 
                and 0 <= cur.y < len(image[cur.x])
                and image[cur.x][cur.y] == COLOR):
            continue
            
        image[cur.x][cur.y] = not COLOR  # flip color
        q.extend([Cell(cur.x - 1, cur.y), Cell(cur.x + 1, cur.y),
                  Cell(cur.x, cur.y - 1), Cell(cur.x, cur.y + 1)])
            
    return


def flip_color_wrapper(x, y, image):
    flip_color(x, y, image)
    return image


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('matrix_connected_regions.py',
                                       'painting.tsv', flip_color_wrapper))
