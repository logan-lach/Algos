def maxProfit(prices) -> int:
    holder = []

    high = prices[0]
    profit = 0

    for i in range(1, len(prices)):
        if high <= prices[i]:
            profit += prices[i] - high
            high = prices[i]

        else:
            holder.append(profit)
            high = prices[i]
            profit = 0

    return holder[-2:]

print(maxProfit([3,3,5,0,0,3,1,4]))