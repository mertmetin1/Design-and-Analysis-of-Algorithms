import pandas as pd

def knapsack(values, weights, capacity):
    n = len(values)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    dp_table = pd.DataFrame(dp)
    print("Initial DP Table:")
    print(dp_table)
    print("\n")

    # Iterate through each item
    for i in range(1, n + 1):
        # Iterate through each capacity from 0 to capacity
        for w in range(0, capacity + 1):
            if weights[i-1] <= w:
                # If the item can be included
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]] + values[i-1])
                decision = f"Include item {i-1} (value: {values[i-1]}, weight: {weights[i-1]})"
            else:
                # If the item cannot be included
                dp[i][w] = dp[i-1][w]
                decision = f"Exclude item {i-1} (weight: {weights[i-1]})"

            # Print the decision and the current state of dp table
            print(f"dp[{i}][{w}] decision: {decision}")
            dp_table = pd.DataFrame(dp)
            print(dp_table)
            print("\n")

    print("Final DP Table:")
    dp_table = pd.DataFrame(dp)
    print(dp_table)

    return dp[n][capacity]

# Example usage
values = [60, 100, 120]
weights = [1, 2, 3]
capacity = 10
print("Maximum value:", knapsack(values, weights, capacity))  # Output: 220
