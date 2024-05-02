def quicksort(A, baslangic, son):
    if baslangic < son:
        # Partition işlemi
        pivot_index = lomuto_partition(A, baslangic, son)
        #pivot_index = hoare_partition(A, baslangic, son)
        # Pivotun etrafındaki alt dizileri sırala
        quicksort(A, baslangic, pivot_index - 1)
        quicksort(A, pivot_index + 1, son)

def lomuto_partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def hoare_partition(arr, low, high):
    pivot = arr[low]
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

# Örnek kullanım
A = [3, 6, 8, 10, 1, 2, 1]
print("Sıralanmamış Dizi:", A)
quicksort(A, 0, len(A) - 1)
print("Sıralanmış Dizi:", A)
