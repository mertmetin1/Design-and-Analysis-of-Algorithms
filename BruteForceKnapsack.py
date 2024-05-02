def BruteForceKnapsack(weights, values, capacity):
    """
    Brute-force approach to solve the knapsack problem using exhaustive search.
    
    Args:
    - weights: A list of n weights w1, w2, ..., wn of n items
    - values: A list of n values v1, v2, ..., vn of n items
    - capacity: The capacity of the knapsack
    
    Returns:
    - max_value: Maximum total value that can be obtained
    - selected_items: List indicating the selected items
    """
    n = len(weights)
    max_value = 0  # Initialize maximum total value to 0
    selected_items = []  # Initialize list of selected items
    
    # Generate all subsets of items using binary representation
    for i in range(2**n):
        subset_weight = 0  # Initialize total weight of current subset
        subset_value = 0  # Initialize total value of current subset
        subset = []  # Initialize list of selected items for current subset
        
        # Convert i to binary representation and pad zeros to the left
        binary_i = bin(i)[2:].zfill(n)
        
        # Iterate through each item and check if it is selected
        for j in range(n):
            if binary_i[j] == '1':
                subset_weight += weights[j]
                subset_value += values[j]
                subset.append(j)  # Add index of selected item to subset
        
        # Check if current subset is feasible (weight <= capacity) and update max_value if applicable
        if subset_weight <= capacity and subset_value > max_value:
            max_value = subset_value
            selected_items = subset
    
    return max_value, selected_items

# Example usage:
weights = [7, 3, 4, 5]  # Example weights of items
values = [42, 12, 40, 25]  # Example values of items
capacity = 10  # Example capacity of knapsack
"""Maximum total value: 65
Selected items: [2, 3]"""
max_value, selected_items = BruteForceKnapsack(weights, values, capacity)
print("Maximum total value:", max_value)
print("Selected items:", selected_items)
