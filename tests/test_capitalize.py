from pg_1.capitalize import capitalize

if capitalize('hello') != 'Hello':
    raise Exception('Функция работает неверно!')

if capitalize('') != '':
    raise Exception('Функция работает неверно!')

if capitalize('3') != '3':
    raise Exception('Функция работает неверно!')

if capitalize('%') != '%':
    raise Exception('Функция работает неверно!')

if capitalize(3) != 3:
    raise Exception('Функция работает неверно!')

if capitalize(2 / 0) is not None:
    raise Exception('Деление на ноль в аргументе!')

print('Все тесты пройдены')
