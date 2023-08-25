with open("new.csv", 'r') as file:
    ls:list = []
    for line in file:
        ls.append(line.split(";"))
        
# так находиться среднее всей таблицы значение строки
s:float = 0.0
all_len:int = 0
for elem in ls:
    if elem[0] != "":
        for i in range(1, len(elem)):
            s += float(elem[i].replace(",", "."))
        # первый столбец не считаем
        # там находиться дата
        all_len += len(elem) - 1

print("Среднее значение:", s/all_len)


# так находиться максимально и миниальное значение во всей таблице
min_value = None
max_value = None

for elem in ls:
    if elem[0] != "":
        if min_value is None or min_value > min(elem):
            min_value = min(elem)
        if max_value is None or max_value < max(elem):
            max_value = max(elem)
            
print("Минимальное значение:", min_value)
print("Максимальное значение", max_value)