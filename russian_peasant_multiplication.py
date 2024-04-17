def russian_peasant_multiplication(a, b):
    result = 0
    print(f"Initial values: a = {a}, b = {b}")
    print("------------------------------------------------------")
    print("|   sayı 1  |   sayı 2   |   Result   |   kalan  |   To Add   |")
    print("------------------------------------------------------")
    while a > 0:
        remainder_value = b if a % 2 == 1 else 0
        print(f"|  {a:^4}  |  {b:^4}  |  {result:^9}  |  {a % 2:^7}  |  {remainder_value:^8}  |")
        result += remainder_value
        a //= 2
        b *= 2
    print("------------------------------------------------------")
    print(f"Final result: {result}")
    return result

# Örnek kullanım
print(russian_peasant_multiplication(623234, 32))
