def recur_method(numb):
    if numb == 1:
        return numb
    else:
        return recur_method(numb - 1) + numb


try:
    numb = int(input('Введите число: '))
    if recur_method(numb) == numb * (numb + 1) / 2:
        print('Равенство верно')
except ValueError:
    print('Вы ввели не цифры. Введите число цифрами')