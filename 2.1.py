def calc():
    operation_type = input('Введите операцию (+, -, *, / или 0 для выхода): ')

    if operation_type == '0':
        return 'Выход'

    else:
        if operation_type in '+-*/':
            try:
                num_1 = int(input('Введите первое число: '))
                num_2 = int(input('Введите второе число: '))

                if operation_type == '+':
                    res = num_1 + num_2
                    print(f'Ваш результат: {res}')
                    return calc()

                elif operation_type == '-':
                    res = num_1 - num_2
                    print(f'Ваш результат: {res}')
                    return calc()

                elif operation_type == '*':
                    res = num_1 * num_2
                    print(f'Ваш результат: {res}')
                    return calc()

                elif operation_type == '/':
                    if num_2 != 0:
                        res = num_1 / num_2
                        print(f'Ваш результат: {res}')
                    else:
                        print('Деление на 0 невозможно')
                    return calc()

            except ValueError:
                print('Вы ввели не цифры. Введите число цифрами')
                return calc()
        else:
            print('Введен неверный символ, попробуйте еще раз')
            return calc()

calc()