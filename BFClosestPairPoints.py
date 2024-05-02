import math

def BruteForceClosestPair(P):
    """
    d(pi , pj ) =   ((xi − xj )2 + (yi − yj ))^(1/2) .
    Brute-force approach to find the distance between the closest pair of points in the plane.
    
    Args:
    - P: A list of n (n ≥ 2) points p1(x1, y1), ..., pn(xn, yn)
    
    Returns:
    - The distance between the closest pair of points
    """
    n = len(P)
    d = float('inf')  # Initialize the minimum distance to positive infinity
    
    # Iterate through all pairs of distinct points
    for i in range(n - 1):
        for j in range(i + 1, n):
            # Compute the Euclidean distance between points i and j
            distance = math.sqrt((P[i][0] - P[j][0])**2 + (P[i][1] - P[j][1])**2)
            # Update the minimum distance if the computed distance is smaller
            d = min(d, distance)
    
    return d

# Example usage:
points = [(0, 0), (1, 1), (2, 2), (3, 3)]  # Example points
closest_distance = BruteForceClosestPair(points)
print("porints:",points)
print("Distance between closest pair of points:", closest_distance)
