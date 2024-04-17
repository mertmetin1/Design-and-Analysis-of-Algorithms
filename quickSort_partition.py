from termcolor import colored

def partition(arr, low, high):
    pivot_index = high
    pivot = arr[pivot_index]
    print(colored("Pivot:", "green"), colored(pivot, "green"), "(index:", colored(pivot_index, "green"), ")")
    print(colored("Array:", "blue"), arr)
    print(colored("Low index:", "cyan"), colored(low, "cyan"))
    print(colored("High index:", "cyan"), colored(high, "cyan"))

    i = low - 1
    for j in range(low, high):
        print()
        print(colored(f"Step {j-low+1}", "yellow"))
        if arr[j] < pivot:
            i += 1
            print(colored("\tArray:", "blue"), arr)
            print(colored(f"\tComparing current element ({arr[j]}) with pivot ({pivot})", "yellow"))
            arr[i], arr[j] = arr[j], arr[i]
            print(colored(f"\tSwapping current element ({arr[i]}) with element ({arr[j]})", "magenta"))
            print(colored("\tArray:", "blue"), arr)
            print(colored(f"\tLow pointer: {i}", "cyan"))
            print(colored(f"\tHigh pointer: {j}", "cyan"))
        else:
            print(colored(f"\tComparing current element ({arr[j]}) with pivot ({pivot})", "red"))
            print(colored("\tArray:", "red"), arr)
            print(colored(f"\tLow pointer: {i}", "cyan"))
            print(colored(f"\tHigh pointer: {j}", "cyan"))

    arr[i + 1], arr[pivot_index] = arr[pivot_index], arr[i + 1]
    print(colored("\tArray after partitioning:", "cyan"), arr)
    print(colored(f"\tSwapping current element ({arr[i + 1]}) with pivot ({pivot})", "magenta"))
    print()

    return i + 1

def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        print(colored("\tPartition index:", "yellow"), colored(pi, "yellow"))
        print(colored("\tLeft partition:", "yellow"), colored(arr[low:pi], "yellow"))
        print(colored("\tRight partition:", "yellow"), colored(arr[pi + 1:high + 1], "yellow"))
        print()

        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)

# Örnek bir liste
arr = [4, 7, 2, 5, 1, 6, 3]

# Sıralama işlemini çağır
print(colored("Initial array:", "red"), arr)
quicksort(arr, 0, len(arr) - 1)

print(colored("Sorted array:", "red"), arr)
