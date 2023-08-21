from itertools import permutations


graf:str = "12 14 21 24 26 35 36 41 42 46 47 53 56 62 63 64 65 67 74 76"
sheme:str ="АБ БА АВ ВА ВД ДВ ВГ ГВ ДЕ ЕД ГЕ ЕГ ЕК КЕ ГК КГ ВЕ ЕВ БВ ВБ"


all_roads:str = "АБВГДЕК"

if len(graf) == len(sheme):
    for var in permutations(all_roads):
        new_graf = graf
        for i in range(len(all_roads)):
            new_graf = new_graf.replace(str(i+1), var[i])
        
        if set(sheme.split()) == set(new_graf.split()):
            print(*[i+1 for i in range(len(all_roads))])
            print(*var)
            print("\n")
else:
    print("Проверь все дороги. Их количество должно совпадать!")