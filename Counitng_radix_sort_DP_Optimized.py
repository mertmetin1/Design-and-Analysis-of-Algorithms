import random

def counting_sort(arr):
    # Find the minimum and maximum values in the array
    min_val = min(arr)
    max_val = max(arr)
    # Determine the size of the count array
    count_size = max_val - min_val + 1
    # Count array to store the frequency of each element
    count = [0] * count_size
    # Output array that will have sorted numbers
    output = []

    # Count the frequency of each element
    for num in arr:
        count[num - min_val] += 1

    # Build the output array
    for i in range(count_size):
        output.extend([i + min_val] * count[i])

    return output

# Rastgele 0 ile 9 arasında değerler içeren bir array oluştur
array = [random.randint(0, 9) for _ in range(10)]
print("Oluşturulan Array:", array)

# Counting sort kullanarak array'i sırala
sorted_array = counting_sort(array)
print("Sıralanmış Array:", sorted_array)
