"""
Nathan Scott
COSC262 Lab 7
Coins Required DP
"""


# def coins_reqd(value, coinage):
#     """A version that doesn't use a list comprehension"""
#     num_coins = [0] * (value + 1)
#     for amt in range(1, value + 1):
#         minimum = None
#         for c in coinage:
#             if c <= amt:
#                 coin_count = num_coins[amt - c]  # Num coins required to solve for amt - c
#                 if minimum is None or coin_count < minimum:
#                     minimum = coin_count
#         num_coins[amt] = 1 + minimum
#     return num_coins[value]


def coins_reqd(value, coinage):
    """Minimum number of coins to represent value, and the coins used.
       Assumes there is a 1-unit coin."""
    num_coins = [0] * (value + 1)
    coin_counts = [{} for _ in range(value + 1)]  # Array of dictionaries to store coin counts

    for amt in range(1, value + 1):
        # Initialize with a large number and an empty dictionary
        min_coins = float('inf')
        min_coin_combination = {}

        for c in coinage:
            if c <= amt:
                # Calculate the new number of coins needed if using coin c
                current_coins = num_coins[amt - c] + 1
                if current_coins < min_coins:
                    min_coins = current_coins
                    # Copy the previous best combination and add the current coin
                    min_coin_combination = coin_counts[amt - c].copy()
                    min_coin_combination[c] = min_coin_combination.get(c, 0) + 1

        # Save the best result for this amount
        num_coins[amt] = min_coins
        coin_counts[amt] = min_coin_combination

    # Prepare the output list from the dictionary of the final amount
    result = [(coin, count) for coin, count in sorted(coin_counts[value].items(), reverse=True)]
    return result


print(coins_reqd(32, [1, 10, 25]))
# print(coins_reqd(6, [1, 2, 6]))
