import math
from typing import List


def coinChange(coins: List[int], amount: int) -> int:
    denominations = dict()
    min_amount = math.inf

    def merge_amounts(A):
        hold = dict()
        for j in A.keys():
            for i in denominations.keys():
                if abs(i-j) >= 0:
                    if abs(i-j) not in denominations.keys():
                        hold[abs(i-j)] = A[j] + denominations[i]
                    else:
                        hold[abs(i-j)] = min(denominations[abs(i-j)], A[j] + denominations[i])
            if j in denominations.keys():
                hold[amount - j] = min(denominations[j], A[j])
            else:
                hold[amount - j] = A[j]
        denominations.update(hold)

        # for i in denominations.keys():
        #     for j in A.keys():
        #         if i + j not in denominations.keys():
        #             denominations[i + j] = A[j] + denominations[i]
        #         else:
        #             denominations[i + j] = min(denominations[i + j], A[j] + denominations[i])
        #         if j in denominations.keys():
        #             denominations[j] = min(denominations[j], A[j])

    for i in range(len(coins) - 1, -1, -1):
        coin = coins[i]
        total_coins = 1
        vals = dict()

        while coin < amount:
            vals[coin] = total_coins
            if coin in denominations.keys():
                min_amount = min(min_amount, total_coins + denominations[coin])
            coin += coins[i]
            total_coins += 1
        merge_amounts(vals)

    return min_amount if min_amount != math.inf else -1


print(coinChange([1,2,5,10],18))
