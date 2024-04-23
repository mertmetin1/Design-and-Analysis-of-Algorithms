def karatsuba(x, y):
    # Tek basamaklı sayılar için çarpım işlemi
    if x < 10 or y < 10:
        return x * y  # Herhangi bir sayı tek basamaklı ise, çarpımı doğrudan döndür

    # Çarpanları iki parçaya ayırma
    m = max(len(str(x)), len(str(y)))  # Çarpanların basamak sayısını bul
    m2 = m // 2  # Basamak sayısının yarısını al, işlem kolaylığı sağlar

    # İki sayıyı iki parçaya ayırma
    high1 = x // 10 ** m2  # İlk sayının yüksek basamaklarını al
    low1 = x % (10 ** m2)  # İlk sayının düşük basamaklarını al
    high2 = y // 10 ** m2  # İkinci sayının yüksek basamaklarını al
    low2 = y % (10 ** m2)  # İkinci sayının düşük basamaklarını al

    # İki parçayı çarparak elde edilen ara terimler
    z0 = karatsuba(low1, low2)  # Düşük basamakların çarpımı
    z1 = karatsuba((low1 + high1), (low2 + high2))  # Düşük ve yüksek basamakların çarpımı
    z2 = karatsuba(high1, high2)  # Yüksek basamakların çarpımı

    # Sonuçları birleştirme
    return (z2 * 10 ** (2 * m2)) + ((z1 - z2 - z0) * 10 ** m2) + z0  # Sonuçları birleştirerek çarpımı döndür


# Örnek kullanım
x = 1234
y = 5678
print("Çarpım:", karatsuba(x, y))  # Karatsuba algoritmasını kullanarak iki sayının çarpımını bul
