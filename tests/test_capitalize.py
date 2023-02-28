from capitalize import capitalize

if capitalize('text') != 'Text':
    raise Exception('Функция работает неверно!')

if capitalize('') != '':
    raise Exception('Функция работает неверно! Нельзя изменить пустую строку.')

print('Все тесты пройдены')
