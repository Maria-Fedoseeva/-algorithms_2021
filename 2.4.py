def recur_method(i, numb, n_count, common_sum):
    if i == n_count:
        print(f'Количество элементов - {n_count}, их сумма - {common_sum}')
    elif i < n_count:
        return recur_method(i + 1, numb / 2 * -1, n_count, common_sum + numb)


try:
    n_count = int(input('Введите количество элементов: '))
    recur_method(0, 1, n_count, 0)
except ValueError:
    print('Вы ввели не цифры. Введите число цифрами')