def orientation(p, q, r):
    """Calculates orientation of triplet (p, q, r)"""
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0  # Collinear
    return 1 if val > 0 else 2  # Clockwise or Counterclockwise


def linear_time_extreme_points(points):
    n = len(points)
    if n < 2:
        return None, None  # Not enough points

    # Find leftmost point
    leftmost_index = min(range(n), key=lambda i: points[i][0])
    reference_point = points[leftmost_index]

    # Initialize extreme points
    extreme_left = None
    extreme_right = None

    for i in range(n):
        # Update extreme left point
        if not extreme_left or orientation(reference_point, points[i], extreme_left) == 2:
            extreme_left = points[i]

        # Update extreme right point
        if not extreme_right or orientation(reference_point, points[i], extreme_right) == 1:
            extreme_right = points[i]

    return extreme_left, extreme_right

# Example usage
points = [(1, 1), (3, 3), (5, 2), (2, 5), (4, 4)]
extreme_left, extreme_right = linear_time_extreme_points(points)
print("Extreme Left Point:", extreme_left)
print("Extreme Right Point:", extreme_right)
