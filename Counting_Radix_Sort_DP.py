import random

def counting_sort(arr):
    # Count array to store the frequency of each element
    count = [0] * 10
    # Output array that will have sorted numbers
    output = []

    # Count the frequency of each element
    for num in arr:
        count[num] += 1
    for i in range(len(count)):
        for k in range(count[i]):
            output.append(i)
    return output

# Rastgele 0 ile 9 arasında değerler içeren bir array oluştur
array = [random.randint(0, 9) for _ in range(10)]
print("Oluşturulan Array:", array)

# Counting sort kullanarak array'i sırala
sorted_array = counting_sort(array)
print("Sıralanmış Array:", sorted_array)
