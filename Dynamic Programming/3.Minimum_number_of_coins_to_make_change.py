def coinChange(coins, money):
    exc = 99999
    ways = [exc] * (money + 1)
    ways[0] = 0
    for denom in coins:
        for amount in range(len(ways)):
            if denom <= amount:
                ways[amount] = min(ways[amount], ways[amount-denom] + 1)
    return -1 if ways[-1] == exc else ways[-1]


if __name__ == "__main__":
    coins = [1,2,4]
    money = 6
    minimum_coins = coinChange(coins, money)
    print(minimum_coins)