def coinChange(coins, amount):
    memo = [-1] * (amount + 1)
    memo[0] = 0  # Base case: 0 coins are needed to make amount 0

    def dp(n):
        if n < 0:
            print(f"dp({n}): Amount is negative, returning infinity")
            return float('inf')  # No solution exists for negative amount
        if memo[n] != -1:
            print(f"dp({n}): Found in memo -> {memo[n]}")
            return memo[n]  # Return the cached result if already computed

        print(f"dp({n}): Computing...")

        min_coins = float('inf')
        for coin in coins:
            print(f"dp({n}): Trying coin {coin}")
            res = dp(n - coin)  # Compute the result for the remaining amount
            if res != float('inf'):
                min_coins = min(min_coins, res + 1)
                print(f"dp({n}): dp({n - coin}) = {res}, min_coins = {min_coins}")

        memo[n] = min_coins  # Store the computed result in memo array
        print(f"dp({n}): Computed result = {min_coins}")
        return memo[n]

    result = dp(amount)
    if result == float('inf'):
        print(f"Result for amount {amount}: No solution (-1)")
        return -1  # If no solution exists
    else:
        print(f"Result for amount {amount}: {result} coins")
        return result

# Test the function
coins = [1, 2, 5]
amount = 11
coinChange(coins, amount)
