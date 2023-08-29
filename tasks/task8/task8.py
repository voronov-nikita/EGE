import itertools


# <------- Задание 1 ------->
s = "1234"

# создаем счетчик
count_varios = 0

for var in itertools.product(s, repeat=5):
    # пишем условие по заданию
    if var.count("1") == 2:
        count_varios += 1

print(count_varios)
# ответ: 270



# <------- Задание 2 ------->
# строка для перебора
s = "ЕГЭ"

# создаем счетчик
count_varios = 0

for var in itertools.product(s, repeat=5):
    # пишем условие по заданию
    if var[0] in ["Е", "Э"]:
        count_varios += 1

print(count_varios)
# ответ: 162



# <------- Задание 3 ------->
# строка для перебора
s = "АОУ"
# создаем счетчик начинающийся с 1
count_varios = 1

# длина опять же равна 5
for var in itertools.product(s, repeat=5):
    if count_varios == 210:
        print(''.join(var))
        # Ответ: УОУАУ
        break
    else:
        count_varios += 1
        