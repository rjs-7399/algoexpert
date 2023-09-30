def make_change(denoms, money):
    ways = [0] * (money + 1)
    ways[0] = 1
    for denom in denoms:
        for amount in range(len(ways)):
            if amount >= denom:
                ways[amount] = ways[amount] + ways[amount - denom]
        print(ways)
    return ways[money]


if __name__ == "__main__":
    denoms = [1, 2, 5]
    money = 5
    ans = make_change(denoms, money)
    print(ans)