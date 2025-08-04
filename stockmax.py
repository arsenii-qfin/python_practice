def stockmax(prices):
    max=0
    profit = []
    profit.append(0)
    for i in prices[::-1]:
        if i > max:
            max = i
        else:
            change = max-i
            profit.append(change)
    return sum(profit)