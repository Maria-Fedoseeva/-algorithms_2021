import time


def time_decorator(func):
    def timer(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        return result, end - start

    return timer


@time_decorator
def list_func(length):
    result = []
    for i in range(length):
        result.append(i)
    return result


@time_decorator
def dict_func(length):
    result = {}
    for i in range(length):
        result[1] = f'number {i}'
    return result

#так тоже не работает(
@time_decorator
def check_dict_key(dict_obj, i):
    print(dict_obj[i])


@time_decorator
def check_list_index(list_obj):
    for i in range(len(list_obj)):
        if i == 3456:
            print(list_obj[i])


@time_decorator
def check_dict_value(dict_obj):
    for v in dict_obj.values():
        if v == 'number 3456':
            print(v)

@time_decorator
def check_list_value(list_obj):
    for v in list_obj:
        if v == 3456:
            print(v)

new_list_1, list_time_1 = list_func(10000)
new_dict_1, dict_time_1 = dict_func(10000)
print('LIST 10000: ', list_time_1)
print('DICT 10000: ', dict_time_1)

new_list_2, list_time_2 = list_func(100000)
new_dict_2, dict_time_2 = dict_func(100000)
print('LIST 100000: ', list_time_2)
print('DICT 100000: ', dict_time_2)

new_list_3, list_time_3 = list_func(1000000)
new_dict_3, dict_time_3 = dict_func(1000000)
print('LIST 1000000: ', list_time_3)
print('DICT 1000000: ', dict_time_3)

# по словарю очевидно дольше
# LIST 10000:  0.000997781753540039
# DICT 10000:  0.0009593963623046875
# LIST 100000:  0.005015373229980469
# DICT 100000:  0.015944719314575195
# LIST 1000000:  0.06584978103637695
# DICT 1000000:  0.17249727249145508

# это вообще не работает, выдало несколько ошибок, я попробовала менять код, но все равно не получилось(
# print('Index LIST 10000: ', check_list_index(new_list_1)[1])
# print('Keys DICT 10000: ', check_dict_key(new_dict_1, 1))
# print('Index LIST 100000: ', check_list_index(new_list_2)[1])
# print('Keys DICT 100000: ', check_dict_key(new_dict_2)[1])
# print('Index LIST 1000000: ', check_list_index(new_list_3)[1])
# print('Keys DICT 1000000: ', check_dict_key(new_dict_3)[1])

print('Values LIST 10000: ', check_list_value(new_list_1)[1])
print('Values DICT 10000: ', check_dict_value(new_dict_1)[1])
print('Values LIST 100000: ', check_list_value(new_list_2)[1])
print('Values DICT 100000: ', check_dict_value(new_dict_2)[1])
print('Values LIST 1000000: ', check_list_value(new_list_3)[1])
print('Values DICT 1000000: ', check_dict_value(new_dict_3)[1])

# как вы определили, что поиск по значениям в словаре дольше, чем в списке, если в результатах замера 0.0?
# Values LIST 10000:  0.0
# Values DICT 10000:  0.0
# Values LIST 100000:  0.0019958019256591797
# Values DICT 100000:  0.0
# Values LIST 1000000:  0.018219470977783203
# Values DICT 1000000:  0.0

# и зачем нужно 3456?