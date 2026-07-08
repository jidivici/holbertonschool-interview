#!/usr/bin/python3
"""
Making change
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total

    Args:
        coins (list): list of the values of the coins in your possession
        total (int): the amount to meet

    Returns:
        int: fewest number of coins needed to meet total
             0 if total is 0 or less
             -1 if total cannot be met by any number of coins
    """
    if total <= 0:
        return 0

    dp = [0] + [float('inf')] * total

    for amount in range(1, total + 1):
        for coin in coins:
            if coin <= amount and dp[amount - coin] + 1 < dp[amount]:
                dp[amount] = dp[amount - coin] + 1

    return dp[total] if dp[total] != float('inf') else -1
