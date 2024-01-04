from pg_1.capitalize import capitalize

assert capitalize('hello') == 'Hello', 'Функция работает неверно!'

assert capitalize('') == '', 'Функция работает неверно!'

assert capitalize('3') == '3', 'Функция работает неверно!'

assert capitalize('%') == '%', 'Функция работает неверно!'

assert capitalize(3) == 3, 'Функция работает неверно!'

assert capitalize(2 / 0) is not None, 'Деление на ноль в аргументе!'

print('Все тесты пройдены')
