import hashlib


s = input('Введите строку из маленьких латинских букв: ')
r = set()
n = len(s)
for i in range(n):
    if i == 0:
        n = len(s) - 1
    else:
        n = len(s)
    for j in range(n, i, -1):
        r.add(hashlib.sha1(s[i:j].encode('utf-8')).hexdigest())

print(f'Количество различных подстрок в строке {s} равно {len(r)}')



s = input('Введите строку из маленьких латинских букв: ')
result_set = set()
for i in range(len(s)):
    last_str = s[i:]
    for length in range(1, len(last_str) + 1):
        sub_str = s[i:i + length]
        if s != sub_str:
            hash_sub_str = hash(sub_str)
            result_set.add(hash_sub_str)


print(f'Количество различных подстрок в строке {s} равно {len(result_set)}')