def factorial(n):
    m = n
    fact = 1
    for i in range(1, m):
        fact *= m
        m -= 1
    print(f'Факториал {n} =', fact)


factorial(int(input('Введите число: ')))
