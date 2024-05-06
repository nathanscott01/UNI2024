"""
Nathan Scott
COSC262 Lab 7
Coins Required DP
"""


def coins_reqd(value, coinage):
    """A version that doesn't use a list comprehension"""
    num_coins = [0] * (value + 1)
    for amt in range(1, value + 1):
        minimum = None
        for c in coinage:
            if c <= amt:
                coin_count = num_coins[amt - c]  # Num coins required to solve for amt - c
                if minimum is None or coin_count < minimum:
                    minimum = coin_count
        num_coins[amt] = 1 + minimum
    return num_coins[value]


# print(coins_reqd(32, [1, 10, 25]))
print(coins_reqd(6, [1, 2, 6]))
