'''
Программа калькулятор. Самое первое приложение на Python
Сначала надо авторизоваться
'''
if input('Введите имя пользователя: ') == 'admin':
    if input('Введите пароль: ') == 'admin':
        print('Вас приветствует калькулятор')
        '''
        Теперь можно посчитать, 2+2=22 ))))).
        '''
        operand_1 = float(input('Введите первый операнд: '))
        action = input('Введите операцию (+, -, *, /): ')
        operand_2 = float(input('Введите второй операнд: '))
        if action == '+':
            print (operand_1 + operand_2)
        elif action == '-':
            print (operand_1 - operand_2)
        elif action == '*':
            print (operand_1 * operand_2)
        elif action == '/':
            if operand_2 != 0:
                print (operand_1 / operand_2)
            else:
                print ('Вы не окончили среднюю школу.')
        else:
            print ('Некорректная операция')
    else:
        print('Некорректный пароль.')
else:
    print('Некорректное имя пользователя.')