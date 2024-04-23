def partition_hoare(arr, low, high):
    pivot = arr[(low + high) // 2]  # Pivot'u dizinin ortasından seçiyoruz
    i = low - 1
    j = high + 1

    while True:
        i += 1
        while arr[i] < pivot:
            i += 1

        j -= 1
        while arr[j] > pivot:
            j -= 1

        if i >= j:
            return j

        arr[i], arr[j] = arr[j], arr[i]


def quicksort_hoare(arr, low, high):
    if low < high:
        pi = partition_hoare(arr, low, high)
        quicksort_hoare(arr, low, pi)
        quicksort_hoare(arr, pi + 1, high)


# Örnek kullanım
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quicksort_hoare(arr, 0, n - 1)
print("Sorted array:", arr)
