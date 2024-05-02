import itertools

def BruteForceTSP(distances):
    """
    Brute-force approach to solve the traveling salesman problem using exhaustive search.
    
    Args:
    - distances: A 2D list representing the distances between cities.
    
    Returns:
    - shortest_distance: Shortest total distance for the tour
    - shortest_tour: List representing the shortest tour
    """
    n = len(distances)
    shortest_distance = float('inf')  # Initialize shortest total distance to positive infinity
    shortest_tour = None  # Initialize shortest tour
    
    # Generate all permutations of intermediate cities (excluding the starting city)
    for permutation in itertools.permutations(range(1, n)):
        tour = [0] + list(permutation) + [0]  # Add starting and ending city to the permutation
        total_distance = 0  # Initialize total distance for the current tour
        
        # Compute the total distance for the current tour
        for i in range(n):
            total_distance += distances[tour[i]][tour[i+1]]
        
        # Update shortest_distance and shortest_tour if current tour is shorter
        if total_distance < shortest_distance:
            shortest_distance = total_distance
            shortest_tour = tour   
    
    return shortest_distance, shortest_tour

# Example usage:
distances = [
    [0, 2, 9, 10],
    [1, 0, 6, 4],
    [15, 7, 0, 8],
    [6, 3, 12, 0]
] 
"""Shortest total distance: 21
Shortest tour: [0, 2, 3, 1, 0]"""

shortest_distance, shortest_tour = BruteForceTSP(distances)
print("Shortest total distance:", shortest_distance)
print("Shortest tour:", shortest_tour)
