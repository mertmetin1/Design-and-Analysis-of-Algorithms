
def is_sorted(arr):
    """
    Function to check if a list is sorted.
    """
    return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))

def exhaustive_sort(arr):
    """
    Brute force approach to sort the input list by trying all permutations.
    """
    import itertools
    
    permutations = itertools.permutations(arr)
    for perm in permutations:
        if is_sorted(perm):
            return list(perm)

# Example usage:
input_list = [4, 2, 8, 1, 3, 5, 9, 6, 7]
sorted_list = exhaustive_sort(input_list)
print("Input:", input_list)
print("Sorted:", sorted_list)
