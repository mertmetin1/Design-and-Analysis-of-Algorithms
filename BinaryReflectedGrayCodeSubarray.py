def gray_code(n):
    if n == 1:
        return ['0', '1']
    else:
        prev_gray = gray_code(n - 1)
        return ['0' + code for code in prev_gray] + ['1' + code for code in reversed(prev_gray)]

# Örnek dizi
arr = [1, 2, 3]

# Diziyi gray_code fonksiyonuna ileterek kodları al
binary_codes = gray_code(len(arr))

# Her bir kod için alt küme oluştur
for code in binary_codes:
    subset = [arr[i] for i in range(len(arr)) if code[i] == '1']
    print(subset)
