# Brute Force yöntemi kullanarak polinom değerini hesapla
def evaluate_polynomial_brute_force(coeffs, x):
    result = 0
    n = len(coeffs)
    for i in range(n):
        # Her bir terimi hesapla ve sonuca ekle
        result += coeffs[i] * (x ** (n - i - 1))
    return result

# Örnek kullanım
polynomial_coeffs = [2, 3, -1, 5]  # Katsayılar: [2, 3, -1, 5]
x_value = 2
result_brute_force = evaluate_polynomial_brute_force(polynomial_coeffs, x_value)
print(f"Brute force yöntemiyle polinomun değeri (x = {x_value}): {result_brute_force}")


# Horner's Rule kullanarak polinom değerini hesapla
def evaluate_polynomial_horner(coeffs, x):
    result = coeffs[0]
    n = len(coeffs)
    for i in range(1, n):
        # Her bir terimi Horner's Rule ile hesapla
        result = result * x + coeffs[i]
    return result

# Örnek kullanım
polynomial_coeffs = [2, 3, -1, 5]  # Katsayılar: [2, 3, -1, 5]
x_value = 2
result_horner = evaluate_polynomial_horner(polynomial_coeffs, x_value)
print(f"Horner's Rule kullanarak polinomun değeri (x = {x_value}): {result_horner}")


def evaluate_polynomial_recursive_horner(coeffs, x, i=0):
    """
    Rekürsif olarak Horner's Rule kullanarak polinomun değerini hesaplar.
    """
    # Base case: Katsayılar dizisi boş ise 0 döndür
    if i == len(coeffs):
        return 0
    
    # Recursive case: Her adımda bir terimi hesapla ve sonuca ekle
    return coeffs[i] + x * evaluate_polynomial_recursive_horner(coeffs, x, i + 1)

# Örnek kullanım
polynomial_coeffs = [2, 3, -1, 5]  # Katsayılar: [2, 3, -1, 5]
x_value = 2
result_recursive_horner = evaluate_polynomial_recursive_horner(polynomial_coeffs, x_value)
print(f"Rekürsif Horner's Rule kullanarak polinomun değeri (x = {x_value}): {result_recursive_horner}")
