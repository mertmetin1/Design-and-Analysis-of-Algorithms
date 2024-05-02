from colorama import Fore, Style
"""    
f(n, k) =

     0 , if n = 1
    
    (f(n - 1, k) + k) mod n , if n > 1
"""
def josephus_recursive(people, k, idx=0):
    if len(people) == 1:
        return people[0]

    idx = (idx + k - 1) % len(people)
    killed_person = people.pop(idx)

    # Diziyi konsola yazdırma
    print(f"Array: {' '.join([f'{Fore.GREEN}[{person}]{Style.RESET_ALL}' if person == killed_person else str(person) for person in people])}")

    # Ölen kişinin adımını yazdırma
    print(f"{Fore.RED}Killed person at step {len(people)}: {killed_person}{Style.RESET_ALL}")

    # Recursive olarak fonksiyonu çağırma
    return josephus_recursive(people, k, idx)

# Josephus problemi için örnek kullanım
n = 12 # Toplam insan sayısı
k = 3  # Her kıyasımda ölen kişi sayısı

people = list(range(1, n + 1))
result = josephus_recursive(people, k)
print(f"The person to survive in Josephus problem with {n} people and killing every {k}th person is: {result}")
