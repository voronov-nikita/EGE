# открываем файл из задния
file = open("demo2024-2.txt")
# запишем в переменную 
ls:str = file.readlines()[0]
# создадим два счетчика - текущего подсчета и максимального подсчета
count:int = 0
max_count:int = -1

# пробегаемся по всем эллементам в нашей строке из файла
for elem in range(1, len(ls)):
    # проверяем одинаковость элементов
    if ls[elem] != ls[elem-1]:
        # если не равны, то прибавить к счетчику
        count += 1
    else:
        # сравниваем текущую максимальную строку с текущем счетчиком
        if max_count < count:
            max_count = count
        # обязательно обнуляем значение счетчика 
        count = 0

# Выводим ответ на 1 больше, так как нам нужна длина, а она начинается не с 0.
print(max_count + 1)