import random
from colorama import Fore, Style

def binary_search_recursive(arr, target, left, right):
    if left <= right:
        mid = (left + right) // 2
        
        # Array'i yazdırma
        print(f"Array: ", end="")
        for i in range(left, right + 1):
            if i == mid:
                print(f"{Fore.GREEN}[{arr[i]}]{Style.RESET_ALL}", end=" ")
            else:
                print(arr[i], end=" ")
        print()
        
        # Min, max, mid ve key değerlerini yazdırma
        print(f"Min: {Fore.BLUE}{arr[left]}{Style.RESET_ALL}, Max: {Fore.BLUE}{arr[right]}{Style.RESET_ALL}, Mid: {Fore.BLUE}{arr[mid]}{Style.RESET_ALL}, Key: {Fore.RED}{target}{Style.RESET_ALL}")
        
        # Orta eleman hedefe eşit mi?
        if arr[mid] == target:
            print(f"{Fore.GREEN}Target {target} found at index {mid}.{Style.RESET_ALL}")
            return mid
        
        # Orta elemandan küçük olan kısmı ara
        elif arr[mid] < target:
            print()
            print(f"{Fore.YELLOW}Searching right half of the array.{Style.RESET_ALL}")
            return binary_search_recursive(arr, target, mid + 1, right)
            
        # Orta elemandan büyük olan kısmı ara
        else:
            print()
            print(f"{Fore.YELLOW}Searching left half of the array.{Style.RESET_ALL}")
            return binary_search_recursive(arr, target, left, mid - 1)
    
    # Hedef dizi içinde bulunamadı
    print()
    print(f"{Fore.RED}Target {target} not found in the array.{Style.RESET_ALL}")
    return -1

# Örnek kullanım
# Rasgele bir dizi oluştur
arr = random.sample(range(1, 99990000000000), 9999000)
# Oluşturulan diziyi sırala
arr.sort()

# Hedef değeri seç
target = random.choice(arr)

# Binary search işlemini gerçekleştir
result = binary_search_recursive(arr, target, 0, len(arr) - 1)
if result != -1:
    print(f"Target {target} found at index {result}.")
else:
    print("Target not found in the array.")