# открываем файл
file = open("17.txt")
# записываем содержимое файла в переменную
ls:list = [int(i) for i in file.readlines()]
# счетчики
count:int = 0
max_summ:int = min(ls)

# перебираем все эллементы
for i in range(1, len(ls)):
    # проверяем по условию
    if ls[i] % 3 == 0 or ls[i-1] % 3 == 0:
        count += 1
        # вычисляем наибольшее число между текущим и суммой двух текущих
        max_summ = max(max_summ, ls[i] + ls[i-1])

# выводим ответ
print(count, max_summ)