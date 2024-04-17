def power(a, n):
    # Baz durum: n sıfırsa, 1'i döndür
    if n == 0:
        print(f"Base case: power({a}, {n}) = 1")
        return 1
    # Tek sayıysa
    elif n % 2 == 1:
        # Recursive olarak n-1'e göre hesapla ve sonucu a ile çarp
        result = a * power(a, (n - 1) // 2) ** 2
        print(f"Odd case: power({a}, {n}) = {a} * power({a}, {(n - 1) // 2}) ** 2 = {result}")
        return result
    # Çift sayıysa
    else:
        # Recursive olarak n/2'ye göre hesapla ve sonucu karesini al
        result = power(a, n // 2) ** 2
        print(f"Even case: power({a}, {n}) = power({a}, {n // 2}) ** 2 = {result}")
        return result

# Örnek kullanım
print(power(3, 4))  # 81 çıktısını verir


