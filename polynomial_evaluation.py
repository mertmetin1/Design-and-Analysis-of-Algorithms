def evaluate_polynomial(coeffs, x):
    result = coeffs[-1]  # İlk başta son terimi al
    print("Başlangıç değeri:", result)

    for i in range(len(coeffs) - 2, -1, -1):  # Terimleri sağdan sola işle
        print("\n{}. terim:".format(len(coeffs) - i - 1))
        print("Eski sonuç:", result)
        print("Katsayı:", coeffs[i])
        print("Eski sonucu x ile çarp:", result, "*", x, "=", result * x)
        print("Katsayıyı ekle:", result * x, "+", coeffs[i], "=", end=" ")
        result = result * x + coeffs[i]  # Yeni sonucu hesapla
        print(result)
    
    return result

# Polinom katsayıları
coefficients = [2, 3, -5, 7]
# Değerlendirilecek x
x_value = 2

# Polinomun değerini hesapla
result = evaluate_polynomial(coefficients, x_value)
print("\nSonuç:", result)
