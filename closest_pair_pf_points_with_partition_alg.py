import math

def euclidean_distance(point1, point2):
    """İki nokta arasındaki Öklid mesafesini hesaplar."""
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def brute_force_closest_pair(points):
    """Brute-force yöntemiyle en yakın çifti bulur."""
    min_distance = float('inf')
    closest_pair = None
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            distance = euclidean_distance(points[i], points[j])
            if distance < min_distance:
                min_distance = distance
                closest_pair = (points[i], points[j])
    return min_distance, closest_pair

def closest_pair_helper(sorted_points, delta, closest_distance, closest_pair):
    """Alt kümedeki en yakın çifti bulur."""
    n = len(sorted_points)
    for i in range(n):
        for j in range(i+1, n):
            if sorted_points[j][1] - sorted_points[i][1] < delta:
                distance = euclidean_distance(sorted_points[i], sorted_points[j])
                if distance < closest_distance:
                    closest_distance = distance
                    closest_pair = (sorted_points[i], sorted_points[j])
    return closest_distance, closest_pair

def closest_pair_recursive(sorted_points):
    """Divide and conquer yöntemiyle en yakın çifti bulur."""
    n = len(sorted_points)
    if n <= 3:
        return brute_force_closest_pair(sorted_points)
    
    mid = n // 2
    left_points = sorted_points[:mid]
    right_points = sorted_points[mid:]
    
    left_distance, left_pair = closest_pair_recursive(left_points)
    right_distance, right_pair = closest_pair_recursive(right_points)
    
    min_distance = min(left_distance, right_distance)
    closest_pair = left_pair if left_distance < right_distance else right_pair
    
    strip = []
    for point in sorted_points:
        if abs(point[0] - sorted_points[mid][0]) < min_distance:
            strip.append(point)
    
    strip.sort(key=lambda x: x[1])
    closest_distance, closest_pair = closest_pair_helper(strip, min_distance, float('inf'), closest_pair)
    
    return closest_distance, closest_pair

def closest_pair(points):
    """En yakın çifti bulur."""
    sorted_points = sorted(points)
    return closest_pair_recursive(sorted_points)

# Örnek kullanım:
points = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
"""En yakın çift: (inf, ((2, 3), (3, 4)))"""
print("En yakın çift:", closest_pair(points))
