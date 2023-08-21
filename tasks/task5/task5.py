def task(n) -> int:
    # преобразовали в двоичном виде и отделим первые два знака
    bin_n = str(bin(n)[2:])
    # находим сумму всех цифр в bin_n и прибавляем в конец
    s1 = sum([int(i) for i in bin_n])
    bin_n += str(s1%2)
    # находим сумму всех цифр в bin_n и прибавляем в конец еще раз
    s2 = sum([int(i) for i in bin_n])
    bin_n += str(s2%2)
    
    # вернет уже преобразованное число
    return int(bin_n, 2)


# прогоним все варианты в цикле
for number in range(1_000):
    r = task(number)
    if r > 43:
        print(r)
        break