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

def quickselect(arr, k):
    low = 0
    high = len(arr) - 1
    while low <= high:
        pi = partition(arr, low, high)
        print(colored("\tPartition index:", "yellow"), colored(pi, "yellow"))
        if pi == k:
            print(colored("\tFound kth smallest element:", "green"), colored(arr[pi], "green"))
            return arr[pi]
        elif pi < k:
            print(colored("\tSearching in the right partition.", "blue"))
            low = pi + 1
        else:
            print(colored("\tSearching in the left partition.", "blue"))
            high = pi - 1
    print(colored("\tCould not find kth smallest element.", "red"))
    return None

# Örnek bir liste
arr = [4, 7, 2, 5, 1, 6, 3]
k = 2  # kth en küçük elemanın indeksi

# Quickselect algoritmasını çağır
print(colored("Initial array:", "red"), arr)
print(colored(f"Finding {k}th smallest element...", "red"))
result = quickselect(arr, k)

if result is not None:
    print(colored(f"{k}th smallest element:", "red"), result)
else:
    print(colored(f"{k}th smallest element not found.", "red"))
