"""
a. Bir n düzenli sihirli bir kare varsa, bu durumda söz konusu toplamın n(n^2 + 1)/2 olduğunu kanıtlayabiliriz.

Bir n düzenli sihirli bir karedeki toplam, her satır, her sütun ve her ana diyagonalde aynı olmalıdır. 
Bu durumda, toplamın her birine dikkat edelim.

    Her satır için toplam: Bu, her satırdaki tüm n sayısının toplamı olacaktır ve bu, 
    n * (n^2 + 1)/2 olacaktır, çünkü satırlardaki tüm sayıların toplamı (n^2 + n)/2 olacaktır ve 
    kher satırda bu toplam elde edilecektir.

    Her sütun için toplam: Satırlardaki toplamı hesaplarken aynı sayıları kullanıyoruz, 
    bu nedenle sütunlardaki toplam da n * (n^2 + 1)/2 olacaktır.

    Ana diyagonal için toplam: Ana diyagonaldeki tüm sayılar aynıdır ve her bir sayı n kez bulunur.
    Bu nedenle, ana diyagonaldeki toplam da n * (n^2 + 1)/2 olacaktır.

Sonuç olarak, bir n düzenli sihirli kare varsa, toplamın n(n^2 + 1)/2 olduğunu kanıtlamış olduk.

b. Tüm n düzenli sihirli kareleri oluşturmak için kaba kuvvet arama algoritması şu adımları izler:

    Bir n x n matris oluşturun ve tüm hücreleri başlangıçta boş olarak işaretleyin.
    Tüm olası permütasyonları ve her bir permütasyonu matrise yerleştirerek tüm olası düzenleri deneyin.
    Her bir düzeni kontrol edin ve sihirli kare olup olmadığını kontrol edin.
    Sihirli kareler bulunduğunda, bunları bir listeye ekleyin.

c. Daha iyi bir algoritma olarak, Sihrili karelerin oluşturulması için daha verimli bir algoritma bulunabilir. 
Örneğin, Sihrili Karelerin oluşturulması için Lo Shu karelerinin metodu kullanılabilir.

d. İki algoritmayı da uygulayıp, 
her birinin bir n düzenli sihirli kare bulmak için kaç dakika sürdüğünü belirlemek için bir deney yapılabilir. 
Bu deney, her iki algoritmanın bir bilgisayar üzerindeki performansını değerlendirebilir ve 
her birinin hangi n değeri için kullanışlı olduğunu belirleyebilir.    
    
    """




import itertools

def is_magic_square(square):
    n = len(square)
    magic_sum = n * (n**2 + 1) // 2
    
    # Her satırın, sütunun ve ana diyagonalin toplamını kontrol et
    for i in range(n):
        row_sum = sum(square[i])
        col_sum = sum(square[j][i] for j in range(n))
        if row_sum != magic_sum or col_sum != magic_sum:
            return False
    
    # Ana diyagonalin toplamını kontrol et
    diag_sum = sum(square[i][i] for i in range(n))
    if diag_sum != magic_sum:
        return False
    
    return True

def generate_magic_squares(n):
    magic_squares = []
    nums = list(range(1, n**2 + 1))
    for perm in itertools.permutations(nums):
        square = [list(perm[i:i+n]) for i in range(0, len(perm), n)]
        if is_magic_square(square):
            magic_squares.append(square)
    return magic_squares

# Örnek kullanım:
n = 3  # 3 düzenli bir sihirli kare oluşturmak için
magic_squares = generate_magic_squares(n)
print(f"Found {len(magic_squares)} magic squares of order {n}:")
for square in magic_squares:
    for row in square:
        print(row)
    print()
