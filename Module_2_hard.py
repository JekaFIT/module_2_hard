def find_pairs(n):
    result = ''
    for a in range(1, 21):
        for b in range(a + 1, 21):
            if (a + b) % n == 0:
                result += f'{a}{b}'
                print(f"Добавлена пара ({a}, {b})")
    return result
n = int(input('Введите число от 3 до 20: '))
result = find_pairs(n)
print(f"Результат для {n}: {result}")
