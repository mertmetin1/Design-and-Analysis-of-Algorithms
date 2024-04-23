def partition_lomuto(arr, low, high):
    pivot = arr[high]  # Pivot'u dizinin son elemanı olarak seçiyoruz
    i = low - 1  # Index'i başlangıç konumuna ayarlıyoruz

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Elemanları yer değiştiriyoruz

    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Pivot'u doğru konuma yerleştiriyoruz
    return i + 1


def quicksort_lomuto(arr, low, high):
    if low < high:
        pi = partition_lomuto(arr, low, high)  # Diziyi böl ve pivot'un index'ini al

        # Pivot'un sol ve sağ alt dizileri için quicksort'u recursive olarak çağır
        quicksort_lomuto(arr, low, pi - 1)
        quicksort_lomuto(arr, pi + 1, high)


# Örnek kullanım
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quicksort_lomuto(arr, 0, n - 1)
print("Sorted array:", arr)
