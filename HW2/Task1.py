n = int(input("Введите число: "))
if n < 0:
    print("Введите число выше ноля")
else:
    print('\n'.join([f'1 * {num} = {num}' for num in range(1, n + 1)]))


# Задача написана с использованием структурной парадигмы, без использования GOTO
# Данные решения относятся к  императивной и декларативной парадигме