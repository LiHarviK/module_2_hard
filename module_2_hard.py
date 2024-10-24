def generate_password(n):
    result = ''
    pairs = []

    for a in range(1, 21):
        if a == n:
            continue
        for b in range(a + 1, 21):
            if b == n:
                continue
            pair_sum = a + b
            if n % pair_sum == 0:
                pairs.append(f'{a}{b}')
    result = ''.join(pairs)
    return result

while True:
    try:
        n = int(input('Введите число от 3 до 20: '))
        if 3 <= n <= 20:
            break
        else:
            print('Нужно ввести число в диапазоне от 3 до 20')
    except ValueError:
        print('Введите корректное целое число')

password = generate_password(n)
print(f'Пароль для числа {n}: {password}')