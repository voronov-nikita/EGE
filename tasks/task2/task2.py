# создаем столько циклов, сколько переменных в нашем выражении
# диапазон 2, потому что принимаюттьяс на вход только 0 и 1
for x in range(2):
    for y in range(2):
        for z in range(2):
            # переписываем выражение на python
            f = (x or y) <= (z==x)
            # так как выражение должно быть отрицательным, мы проверяем чере зотрицание
            if not f:
                # строка ниже должна будет меняться в зависимости от вашего представления и стравнения
                print(x, z, y)
                # 0 1 1
                # 1 0 0
                # 1 0 1
                