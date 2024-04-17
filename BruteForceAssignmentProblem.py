import itertools

def BruteForceAssignmentProblem(cost_matrix):
    """
    Brute-force approach to solve the assignment problem using exhaustive search.
    
    Args:
    - cost_matrix: A 2D list representing the cost matrix C[i, j] for each pair i, j = 1, 2, ..., n
    
    Returns:
    - min_cost: Minimum total cost
    - min_assignment: Tuple indicating the assignment with the minimum total cost
    """
    n = len(cost_matrix)
    min_cost = float('inf')  # Initialize minimum total cost to positive infinity
    min_assignment = None  # Initialize minimum assignment
    
    # Generate all permutations of integers 0 to n-1 representing the assignments
    permutations = itertools.permutations(range(n))
    
    # Iterate through each permutation
    for assignment in permutations:
        total_cost = 0  # Initialize total cost for current assignment
        
        # Compute the total cost for the current assignment
        for i in range(n):
            total_cost += cost_matrix[i][assignment[i]]
        
        # Update minimum total cost and assignment if current total cost is smaller
        if total_cost < min_cost:
            min_cost = total_cost
            min_assignment = assignment
    
    return min_cost, min_assignment

# Example usage:
cost_matrix = [
    [9, 6, 5, 7],
    [2, 4, 8, 6],
    [7, 3, 1, 9],
    [8, 7, 8, 4]
]

min_cost, min_assignment = BruteForceAssignmentProblem(cost_matrix)
print("Minimum total cost:", min_cost)
print("Minimum assignment:", min_assignment)
