from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:
    current_min = prices[0]
    max_profit = 0.0
    
    for i in range(1, len(prices)):
        if prices[i] < current_min:
            current_min = prices[i]
        
        max_profit = max(max_profit, prices[i] - current_min)

    return max_profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
