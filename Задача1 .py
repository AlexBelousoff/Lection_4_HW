t = 'Hillel school'
# функция str.len - длина строки
# d = len(t)
# print(d)

stroke = t[:2] + t[11:]
s = len(stroke)
# print(s)

if s < 2:
    print('Ваша стока слишком короткая')
else:
    print(stroke)
