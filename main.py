import random

# Набор доступных символов.
ARRAY_SYMBOLS = [
    '0', '1', '2', '3', '4',
    '5', '6', '7', '8', '9',
    'a', 'b', 'c',
    'A', 'B', 'C',
    '!', '@']

# Получаем количество символов в пароле.
COUNT_SYMBOLS = 4
input_count = input('Введите количество символов в пароле: ')
if input_count.isdigit():
    count_symbols = int(input_count)
else:
    count_symbols = COUNT_SYMBOLS

# Узнаем количество всех возможных комбинаций.
count_variant = len(ARRAY_SYMBOLS) ** count_symbols


# Получить случайный символ.
def random_symbols():
    return ARRAY_SYMBOLS[
        random.randint(0, len(ARRAY_SYMBOLS) - 1)
    ]


print(f'Количество доступных сиволов: {len(ARRAY_SYMBOLS)}')
print(f'Доступные сиволы: {(ARRAY_SYMBOLS)}')
print(f'Количество возможных комбинаций: {count_variant}')

password = ''

# Генирируем уникальный пароль.
for i in range(0, count_symbols):
    password = password + f'{random_symbols()}'

print(f'Сгенерированный пароль: {password}')

# Запись пароля в файл.
with open('password.txt', 'a') as password_string:
    password_string.write('{}\n'.format(f'{password}'))
