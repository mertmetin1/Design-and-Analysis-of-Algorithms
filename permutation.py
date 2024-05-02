



permutedlist=[]
def permute(elements, start=0):
    
    if start == len(elements):
        permutedlist.append(elements)
        #print(permutedlist)
        print(elements)
    else:
        for i in range(start, len(elements)):
            # Elemanların yerlerini değiştir
            elements[start], elements[i] = elements[i], elements[start]
            # Rekürsif olarak permütasyonları oluştur
            permute(elements, start + 1)
            # Yerleri değiştirilmiş elemanları geri değiştir
            elements[start], elements[i] = elements[i], elements[start]
    return permutedlist

def heap_permute(n, A):
    # Base case: if n is 1, print the permutation
    if n == 1:
        print(A)
    else:
        for i in range(n):
            heap_permute(n - 1, A)
            if n % 2 == 0:  # if n is even
                A[i], A[n-1] = A[n-1], A[i]
            else:  # if n is odd
                A[0], A[n-1] = A[n-1], A[0]

def lexicographic_permute(arr):
    n = len(arr)
    
    yield arr[:]  # Başlangıç permütasyonunu üret
    
    while True:
        # Son permütasyonun ardışık iki elemanı artan sırada mı kontrol et
        for i in range(n-2, -1, -1):
            if arr[i] < arr[i+1]:
                break  # İkili artan sıra bulundu
        
        else:
            break  # Artan sıra yok, döngüyü sonlandır
        
        # Ai'yi arttır ve permütasyonu güncelle
        for j in range(n-1, i, -1):
            if arr[j] > arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
                arr[i+1:] = arr[i+1:][::-1]  # Sona kadar olan kısmı ters çevir
                break
        
        yield arr[:]  # Yeni permütasyonu üret

def johnson_trotter(arr):
    n = len(arr)
    direction = [False] * n  # False sağa doğru, True sola doğru
    
    yield arr[:]  # Başlangıç permütasyonunu üret
    
    while True:
        largest_mobile = -1
        # En büyük hareketli elemanı bul
        for i in range(n):
            if (i == 0 or arr[i] > arr[i-1]) and \
               (i == n-1 or arr[i] > arr[i+1]):
                if largest_mobile == -1 or arr[i] > arr[largest_mobile]:
                    largest_mobile = i
        
        if largest_mobile == -1:
            break  # Hareketli eleman kalmadığında döngüyü sonlandır
        
        # Yönü değiştir
        if largest_mobile > 0 and direction[arr[largest_mobile] - 1]:
            arr[largest_mobile], arr[largest_mobile-1] = arr[largest_mobile-1], arr[largest_mobile]
            direction[arr[largest_mobile-1] - 1] = not direction[arr[largest_mobile-1] - 1]
        elif largest_mobile < n-1 and not direction[arr[largest_mobile] - 1]:
            arr[largest_mobile], arr[largest_mobile+1] = arr[largest_mobile+1], arr[largest_mobile]
            direction[arr[largest_mobile] - 1] = not direction[arr[largest_mobile] - 1]
        
        yield arr[:]  # Yeni permütasyonu üret



